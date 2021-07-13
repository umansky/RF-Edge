com.nycore[0]=16; com.nysol[0]=32; com.nxleg[0,1]=24; com.nxcore[0,1]=24
bbb.restart=1; bbb.newgeo=1; bbb.icntnunk=0
bbb.dtreal = 1e-14; bbb.ftol=1e-10
bbb.exmain()
hdf5_save("mycase_hr.h5")



com.nycore[0]=32; com.nysol[0]=64; com.nxleg[0,1]=48; com.nxcore[0,1]=48
bbb.restart=1; bbb.newgeo=1; bbb.icntnunk=0
bbb.dtreal = 1e-14; bbb.ftol=1e-10
bbb.exmain()
hdf5_save("mycase_hhr.h5")
