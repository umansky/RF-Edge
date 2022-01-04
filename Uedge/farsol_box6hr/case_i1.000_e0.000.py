#exec(open("case_i1.000_e0.000.py").read())

from runcase import *
from vorpal2uedge import *


exec(open("./run2steady.py").read())
ni_orig=(bbb.ni).copy()
up_orig=(bbb.up).copy()
te_orig=(bbb.te).copy()
ti_orig=(bbb.ti).copy()
###mu.paws()


#ifile='/home/umansky1/Collaboration/TomJenkins/RF-Edge.6dec2021/Uedge/farsol_box6hr/ion_data.h5'
#efile='/home/umansky1/Collaboration/TomJenkins/RF-Edge.6dec2021/Uedge/farsol_box6hr/electron_data.h5'
ifile='./ion_data.h5'
efile='./electron_data.h5'
uefile="tmp_i1.000_e0.0.h5"


Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=ifile)
val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
pondomfpari_use=np.nan_to_num(val) ##-save it for later for scaling etc.
bbb.pondomfpari_use[:,:,0]=1.00*pondomfpari_use

Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=efile)
val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
pondomfpare_use=np.nan_to_num(val) ##-save it for later for scaling etc.                                            
bbb.pondomfpare_use[:,:]=0.00*pondomfpare_use

hdf5_restore(uefile)
bbb.dtreal=1e20; bbb.exmain()

##-now analyze the results, e.g.,
##plt.plot(bbb.ni[:,20,0]); plt.plot(ni_orig[:,20,0]); plt.show()
#
#deltan=(bbb.ni-ni_orig)/ni_orig
#mp.plotvar(deltan[:,:,0])
#
#deltaup=(bbb.up-up_orig)
#mp.plotvar(deltaup[:,:,0], iso=False)
