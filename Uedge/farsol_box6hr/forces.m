clear;close all;format long e;
% load the history file to get the normalization
fname='nstxEdge_History.h5';
P=h5read(fname,'/poynFluxFromAntennaAperture');
P=P';
dt=1e-12; % from input file
lP=length(P);
t=0:dt:(lP-1)*dt;

sw=2;
if sw==1
Pa=zeros(size(P));
nav=33333; %35001;
nh=(nav-1)/2;
for q=nh+1:lP-nh
 Pa(q)=sum(P(q-nh:q+nh))/nav;
end;
end;

figure(1);
set(gcf,'WindowStyle','docked','Color','white')
plot(t,P,'r-','LineWidth',2)
if sw==1
hold on
plot(t,Pa,'b-','LineWidth',2);
disp('Paused!')
pause
end;

% finding - Pa ~ -19.98, so need to multiply by 1e6/19.98 = 5.005e4
nf=5.005e4;

Fionr=zeros(303,817,20);
Fionp=Fionr;
Fionx=Fionr;

elec=1; % 1 for electrons, anything else for ions

qlist=[1 8 15 2 9 16 3 10 17 4 11 18 5 12 19 6 13 20 7 14];
for q=395:414
  if elec==1
  fname=strcat('nstxEdge_FpondElectron_',int2str(q),'.h5');
  Fion=h5read(fname,'/FpondElectron');
  else
  fname=strcat('nstxEdge_FpondIon1_',int2str(q),'.h5');
  Fion=h5read(fname,'/FpondIon1');
  end;
  %for rr=1:303
  % for ss=1:817
  %  for tt=1:3
  %  if abs(Fion(tt,ss,rr)*nf)>1e2
  %   Fion(tt,ss,rr)=0;
  %  end;
  %  end;
  % end;
  %end;
  Fionr(:,:,q-394)=squeeze(Fion(1,:,:))';
  Fionp(:,:,q-394)=squeeze(Fion(2,:,:))'/sqrt(2)+squeeze(Fion(3,:,:))'/sqrt(2);
  Fionx(:,:,q-394)=squeeze(Fion(2,:,:))'/sqrt(2)-squeeze(Fion(3,:,:))'/sqrt(2);
end;

lx=.755;
xs=-.205;
nx=302;
dx=lx/nx;
x=xs:dx:xs+lx;
ly=2.04;
ys=-1.02;
ny=816;
dy=ly/ny;
y=ys:dy:ys+ly;
[Y,X]=meshgrid(y,x);

FionpNorm=Fionp*nf;
FionpAv=sum(FionpNorm,3)/20;
FionrNorm=Fionr*nf;
FionrAv=sum(FionrNorm,3)/20;
FionxNorm=Fionx*nf;
FionxAv=sum(FionxNorm,3)/20;


for qq=1:303
 for rr=1:817
  if abs(FionpAv(qq,rr))>100
   FionpAv(qq,rr)=NaN;
  end
 end
end

Fmaxr=max(max(max(FionpAv)));
Fminr=min(min(min(FionpAv)));

%A=stlread('nstxEdgePecShapes.stl');
W=h5read('nstxEdge_nstxFakeWall_0.h5','/nstxFakeWall');

figure(2);
set(gcf,'WindowStyle','docked','Color','white')
%trisurf(A,'FaceColor','black');
hold on;
surf(X,Y,0*FionpAv,FionpAv);
%trisurf(A,'FaceColor','black');
shading interp
view(0,90);
set(gca,'CLim',[Fminr Fmaxr]);
colorbar;
axis equal
drawnow

if elec==1
 title('Electron parallel ponderomotive force')
 set(gca,'CLim',[Fminr Fmaxr]/80);
 fname='electron_data.h5';
else
 title('Ion parallel ponderomotive force');
 fname='ion_data.h5';
 set(gca,'CLim',[-2e-2 2e-2])
end;

if(exist(fname))
 eval(strcat(['!rm ',fname]));
 disp('removed old file')
end

h5create(fname,'/Xgrid',[nx+1 ny+1]);
h5create(fname,'/Ygrid',[nx+1 ny+1]);
h5create(fname,'/Fradial',[nx+1 ny+1]);
h5create(fname,'/Fperp',[nx+1 ny+1]);
h5create(fname,'/Fparallel',[nx+1 ny+1]);

h5write(fname,'/Xgrid',X);
h5write(fname,'/Ygrid',Y);
h5write(fname,'/Fradial',FionrAv);
h5write(fname,'/Fperp',FionxAv);
h5write(fname,'/Fparallel',FionpAv);