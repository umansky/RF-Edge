import uedge_mvu.idealgrid as mid
from runcase import *
exec(open("./run2steady.py").read())
mu.paws("Expecting a steady-state solution at this point")


#-modify the poloidal grid
mid.idlg_ModPol(ixmin=15,ixmax=45, alfxt=1.95, smoothe=True)
mid.idlg_Write(fname="gridue.mod2", runid="mod2.grid")
bbb.GridFileName="gridue.mod2"
bbb.gengrid=0; bbb.newgeo=1
#bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
#rundt(1e-8)
hdf5_restore("mod2.h5")
bbb.exmain(); mu.paws("check point 1")


##-modify the grid
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=0.0)
mid.idlg_Write(fname="gridue.mod3", runid="mod3.grid")
bbb.GridFileName="gridue.mod3"
bbb.gengrid=0; bbb.newgeo=1
#bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
#rundt(1e-8)
hdf5_restore("mod3.h5")
bbb.exmain(); mu.paws("check point 2")


#-modify the radial grid further
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=-0.05)
mid.idlg_Write(fname="gridue.mod3.005", runid="mod3.005.grid")
bbb.GridFileName="gridue.mod3.005"
bbb.gengrid=0; bbb.newgeo=1
hdf5_restore("mod3.005.h5")
bbb.exmain(); mu.paws("check point 3")


#-modify the radial grid further                                                                                     
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=-0.09)
mid.idlg_Write(fname="gridue.mod3.009", runid="mod3.009.grid")
bbb.GridFileName="gridue.mod3.009"
bbb.gengrid=0; bbb.newgeo=1
hdf5_restore("mod3.009.h5")
bbb.exmain(); mu.paws("check point 4")
