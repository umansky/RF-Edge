grd.radm=-0.05; grd.radx=0.05; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp1.h5')
mu.paws()

grd.radm=-0.05; grd.radx=0.05; bbb.newgeo=1; bbb.isbcwdt=1;
grd.radx=0.05; com.nysol[0]=8
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp2.h5')
mu.paws()

grd.radm=-0.05; grd.radx=0.06; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp3.h5')
mu.paws()

grd.radm=-0.05; grd.radx=0.07; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp4.h5')
mu.paws()

grd.radm=-0.05; grd.radx=0.08; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp5.h5')
mu.paws()


bbb.recycp=0.9
grd.radm=-0.05; grd.radx=0.10; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp6.h5')
mu.paws()


bbb.recycp=0.9
grd.radm=-0.05; grd.radx=0.15; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp6.h5')
mu.paws()


bbb.recycp=0.9
grd.radm=-0.05; grd.radx=0.20; bbb.newgeo=1; bbb.isbcwdt=1;
bbb.dtreal=1e-10; bbb.exmain()
rundth(1e-10)
hdf5_save('tmp7.h5')
mu.paws()
