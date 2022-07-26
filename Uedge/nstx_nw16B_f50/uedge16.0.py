import uedge_mvu.idealgrid as mid
from runcase import *
exec(open("./run2steady.py").read())
mu.paws("Restored the base case")


#-modify the poloidal grid                                                          
mid.idlg_ModPol(ixmin=15,ixmax=45, alfxt=1.95, smoothe=True)

#-modify the radial grid                                      
mid.idlg_ModRad(jymin=10,jymax=20, alfyt=-0.2)

#-save the new grid
mid.idlg_Write(fname="gridue.mod3.02", runid="mod3.02.grid")

#-run on the new grid
bbb.GridFileName="gridue.mod3.02"
bbb.gengrid=0; bbb.newgeo=1
hdf5_restore("uedge16.0.h5")
bbb.dtreal=1e20; bbb.exmain()
