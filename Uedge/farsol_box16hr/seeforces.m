clear;close all;format long e;

nxcells=302;
nycells=816;
lx=.755;
ly=2.04;
xbgn=-.205;
ybgn=-1.02;
dx=lx/nxcells;
dy=ly/nycells;
x=xbgn:dx:xbgn+lx;
y=ybgn:dy:ybgn+ly;
[Y,X]=meshgrid(y,x);

% load the history file to get the normalization
fname='nstxEdge_History.h5';
%fname='stuff.h5'
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

% finding - Pa ~ -21.246, so need to multiply by 1e6/21.246 = 4.707e4
nf=4.707e4;

%nint=h5read('nstxEdge_nodeInteriorness_0.h5','/nodeInteriorness');
%nint=(squeeze(nint))';

Fpe=zeros(303,817);
Fpi=zeros(303,817);

ilist=[14 1 8 15 2 9 16 3 10 17 4 11 18 5 12 19 6 13 20 7];
for q=1:length(ilist)
 qq=359+ilist(q);
 fname=strcat('nstxEdge_FpondElectron_',int2str(qq),'.h5');
 Fe=h5read(fname,'/FpondElectron');
 Fex=squeeze(Fe(1,:,:))';
 Fey=squeeze(Fe(2,:,:))';
 Fez=squeeze(Fe(3,:,:))'; 
 fname=strcat('nstxEdge_FpondIon1_',int2str(qq),'.h5');
 Fi=h5read(fname,'/FpondIon1');
 Fix=squeeze(Fi(1,:,:))';
 Fiy=squeeze(Fi(2,:,:))';
 Fiz=squeeze(Fi(3,:,:))';
 % average, with normalization, over all 20 dumps
 Fpe=Fpe+(Fey/sqrt(5)+2*Fez/sqrt(5))/20*nf;
 Fpi=Fpi+(Fiy/sqrt(5)+2*Fiz/sqrt(5))/20*nf;
end

figure(1);
set(gcf,'WindowStyle','Docked','color','white');
surf(X,Y,0*X,Fpi)
shading interp
view(0,90);
axis equal
set(gca,'XLim',[-.05 .58],'YLim',[-.66 -.23])
title('Ion force')

figure(2);
set(gcf,'WindowStyle','Docked','color','white');
surf(X,Y,0*X,Fpe)
shading interp
view(0,90);
axis equal
set(gca,'XLim',[-.05 .58],'YLim',[-.66 -.23])
title('Electron force')

sw=1;
if sw==2
 fname='tmp_difni_3.000000.h5';
 rm=h5read(fname,'/com/rm');
 zm=h5read(fname,'/com/zm');
 r1=squeeze(rm(1,:,:));
 z1=squeeze(zm(1,:,:));
 [sz1a,sz1b]=size(z1);
 %z1(1,:)=z1(2,:);
 %z1(sz1a,:)=z1(sz1a-1,:);

 Fiuedge=interp2(X',Y',Fpi',r1',z1');
 Feuedge=interp2(X',Y',Fpe',r1',z1');
 Fiuedge=Fiuedge';
 Feuedge=Feuedge';

 for qx=1:22
  for qy=1:90
   if abs(Feuedge(qx,qy))>1e5
    Feuedge(qx,qy)=0;
   end
  end
 end
 for qx=1:22
  for qy=1:90
   if abs(Fiuedge(qx,qy))>1e5
    Fiuedge(qx,qy)=0;
   end
  end
 end

 % okay, now write to an h5 file
 ! rm VorpalDataOnUedgeGrid.h5
 h5create('VorpalDataOnUedgeGrid.h5','/xgrid',[sz1a sz1b]);
 h5create('VorpalDataOnUedgeGrid.h5','/ygrid',[sz1a sz1b]);
 h5create('VorpalDataOnUedgeGrid.h5','/pfIpar',[sz1a sz1b]);
 h5create('VorpalDataOnUedgeGrid.h5','/pfEpar',[sz1a sz1b]);
 h5write('VorpalDataOnUedgeGrid.h5','/xgrid',r1);
 h5write('VorpalDataOnUedgeGrid.h5','/ygrid',z1);
 h5write('VorpalDataOnUedgeGrid.h5','/pfIpar',Fiuedge);
 h5write('VorpalDataOnUedgeGrid.h5','/pfEpar',Feuedge);
end % sw

