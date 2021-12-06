clear;close all;format long e;
qlist=[1 8 15 2 9 16 3 10 17 4 11 18 5 12 19 6 13 20 7 14];

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

for hhh=1:10
for q=1:20
 fnum=qlist(q)+395;
 fname=strcat('nstxEdge_E_',int2str(fnum),'.h5');
 EV=h5read(fname,'/E');
 Ex=squeeze(EV(1,:,:))';
 Ey=squeeze(EV(2,:,:))';
 Ez=squeeze(EV(3,:,:))';
 figure(1);
 set(gcf,'WindowStyle','Docked','color','white');
 surf(X,Y,Ey)
 shading interp
 view(0,90);
 set(gca,'ZLim',[-650 650],'CLim',[-650 650]/50);
 set(gca,'XLim',[-1.087561892610891e+00     1.432561892610891e+00])
 set(gca,'YLim',[-1.02 1.02])
 colorbar
 drawnow
 pause(.1)
end
end % hhh