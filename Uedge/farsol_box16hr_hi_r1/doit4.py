import uedge_mvu.idealgrid as mid
from runcase import *
exec(open("./run2steady.py").read())
#-should be a steady-state solution at this point


#-modify the poloidal grid
mid.idlg_ModPol(ixmin=15,ixmax=45, alfxt=1.95, smoothe=True)
mid.idlg_Write(fname="gridue.mod2", runid="mod2.grid")
bbb.GridFileName="gridue.mod2"
bbb.gengrid=0; bbb.newgeo=1
bbb.exmain()



##-modify the grid
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=0.0)
mid.idlg_Write(fname="gridue.mod3", runid="mod3.grid")
bbb.GridFileName="gridue.mod3"
bbb.gengrid=0; bbb.newgeo=1
bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
rundt(1e-8)
hdf5_save("mod3.h5")


#-modify the radial grid further
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=-0.1)
mid.idlg_Write(fname="gridue.mod3.01", runid="mod3.01.grid")
bbb.GridFileName="gridue.mod3.01"
bbb.gengrid=0; bbb.newgeo=1
bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
rundt(1e-8)
hdf5_save("mod3.01.h5")


#-modify the radial grid further                                                                                
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=-0.2)
mid.idlg_Write(fname="gridue.mod3.02", runid="mod3.02.grid")
bbb.GridFileName="gridue.mod3.02"
bbb.gengrid=0; bbb.newgeo=1
bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
rundt(1e-8)
hdf5_save("mod3.02.h5")
