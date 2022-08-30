clear;close all;format long e;

fname='uedge17.1.h5' % Maxim's intermediate-edge-density, nonuniform-grid case

% read the density and grid data and rearrange
rm=h5read(fname,'/com/rm');
zm=h5read(fname,'/com/zm');
r1=squeeze(rm(1,:,:));
z1=squeeze(zm(1,:,:));
ax=min(min(min(rm)));
ay=min(min(min(zm)));
nia=h5read(fname,'/bbb/ni');
ni=squeeze(nia(1,:,:));

% Compare with the Vorpal grid (next three lines from input file)
disp('Are these the input file values?');
  numCells = [564 1632  12]
  lengths = [0.705 2.04 0.03]
  startPositions = [-0.205 -1.02 -0.015]
disp('If not, change the matlab code.');

% Set sw=1 to write a new file for Vorpal from the UEDGE data
% Set sw=0 to debug
sw=1;

%  build the vorpal grid
dxvals=lengths./numCells;
xvg=startPositions(1):dxvals(1):startPositions(1)+lengths(1);
yvg=startPositions(2):dxvals(2):startPositions(2)+lengths(2);
[Yvg,Xvg]=meshgrid(yvg,xvg);
[sz1a,sz1b]=size(z1);

% regularize the uedge grids, there are a few values with some
% roundoff that matlab doesn't know how to handle
z1(1,:)=z1(2,:);
z1(sz1a,:)=z1(sz1a-1,:);
r1(:,1)=r1(:,2);
r1(:,sz1b)=r1(:,sz1b-1);

% interpolate the uedge grid to the vorpal grid, putting zero
% everywhere outside
Nigrid=interp2(z1,r1,ni,Yvg,Xvg,'linear',0);
asum=0;
ind=1;
[nzg,nrg]=size(Nigrid);

% find the places outside the grid on the left, where ni was set
% to zero, and map the first nonzero values we find as we move
% rightwards in x back onto those points.
% first find the points:
while asum==0
 asum=sum(Nigrid(ind,:));
 ind=ind+1;
end
ind=ind-1
% then do the mapping.
% three gridpoints on the top and bottom have no density
% because they are inside of metal
for q=ind-1:-1:1
 Nigrid(q,1+3:nrg-3)=(3*Nigrid(q+1,1+3:nrg-3)-3*Nigrid(q+2,1+3:nrg-3)+Nigrid(q+3,1+3:nrg-3));
 %q
 %pause
end

% find the places outside the grid on the right, where ni was
% set to zero, and continue the exponential decay.
% first find the points:
asum=0;
ind=nzg;
while asum==0
 asum=sum(Nigrid(ind,:));
 ind=ind-1;
end;
ind=ind+1;

% exponential is linear in log space
LNigrid=log(Nigrid);
for q=ind+1:nzg
 % linear extrapolation
 LNigrid(q,:)=2*LNigrid(q-1,:)-LNigrid(q-2,:);
end
Nigrid=exp(LNigrid);

% reshape the arrays
Xvg=Xvg';
Yvg=Yvg';
Nigrid=Nigrid';

% We've got NaN's where there is zero density because of the way
% we did the extrapolation on the antenna side, so get rid of those.
% They only happen inside the metal wall.
for qx=1:numCells(2)+1
 for qy=1:numCells(1)+1
  if isnan(Nigrid(qx,qy))==1
   Nigrid(qx,qy)=0.;
  end
 end
end

figure(1);
set(gcf,'WindowStyle','Docked','color','white');
% plot the vorpal data
surf(Xvg,Yvg,Nigrid);
view(0,90)
hold on
% plot a bounding box for the UEDGE data
plot3([-.05 .4 .4 -.05 -.05],[-1 -1 1 1 -1],1e20*[1 1 1 1 1],'r-')
set(gca,'ZScale','log')
view(0,0)
shading interp
% plot the UEDGE data
surf(r1,z1,ni);

if sw==1 % write a new data file for vorpal
 Xvge(1,:,:)=Xvg;
 Xvge(2,:,:)=Xvg;
 Yvge(1,:,:)=Yvg;
 Yvge(2,:,:)=Yvg;
 Nvge(1,:,:)=Nigrid;
 Nvge(2,:,:)=Nigrid;
 ! rm mycaseOnVorpalGrid.h5
 h5create('mycaseOnVorpalGrid.h5','/xgrid',[2 nrg nzg]);
 h5create('mycaseOnVorpalGrid.h5','/ygrid',[2 nrg nzg]);
 h5create('mycaseOnVorpalGrid.h5','/ngrid',[2 nrg nzg]);
 h5write('mycaseOnVorpalGrid.h5','/xgrid',Xvge);
 h5write('mycaseOnVorpalGrid.h5','/ygrid',Yvge);
 h5write('mycaseOnVorpalGrid.h5','/ngrid',Nvge);
end
