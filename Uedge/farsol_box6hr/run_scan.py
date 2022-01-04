#exec(open("run_scan1.py").read())

from runcase import *
from vorpal2uedge import *

exec(open("./run2steady.py").read())
bbb.dtreal=1e20; bbb.exmain()

ni_orig=(bbb.ni).copy()
up_orig=(bbb.up).copy()
te_orig=(bbb.te).copy()
ti_orig=(bbb.ti).copy()
mu.paws()                                                                                                                                        
  


ifile='./ion_data.h5'
efile='./electron_data.h5'
uefile="mtmp_i0.020_e0.0.h5"


Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=ifile)
val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
pondomfpari_use=np.nan_to_num(val) ##-save it for later for scaling etc.                                                                            
  
Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=efile)
val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
pondomfpare_use=np.nan_to_num(val) ##-save it for later for scaling etc.                                                                            

#hdf5_restore(uefile)
#i=2
#ionFrac=i/100.
#bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*ionFrac
#bbb.pondomfpare_use[:,:]=pondomfpare_use*0.0
#bbb.exmain()
mu.paws("Starting scan now")




for i in range(1,101):
    #
    ionFrac=i/100.
    bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*ionFrac
    bbb.pondomfpare_use[:,:]=pondomfpare_use*0.0
    #
    bbb.dtreal=1e-6; bbb.exmain()
    rundt(1e-6)
    #
    fname="./mtmp_i"+ "{:.3f}".format(ionFrac) +"_e0.0.h5"
    print("Saving in file ", fname)
    hdf5_save(fname)
    ###mu.paws()
