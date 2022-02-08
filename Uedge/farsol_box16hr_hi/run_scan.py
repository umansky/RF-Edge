from runcase import *
exec(open("./run2steady.py").read())
exec(open("vorpal2uedge.py").read())
from filter2d import *
mu.paws()


#-scale down the forces, to simplify convergence
bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*0.0
bbb.pondomfpare_use[:,:]=1e-1*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], width=0.1, x0=0.45, y0=-0.45)
mp.plotvar(bbb.pondomfpare_use,iso=False, vmax=1e-4,vmin=-1e-4)


for i in range(1,11):
    #
    ionFrac=0.0
    elFrac=i/10.
    
    bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*ionFrac
    bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], width=0.1, x0=0.45, y0=-0.45)
    #
    bbb.isbcwdt=1; bbb.dtreal=1e-10; bbb.exmain()
    rundt(1e-8)
    #
    fname="./mtmp_e"+ "{:.3f}".format(elFrac) +"_e0.0.h5"
    print("Saving in file ", fname)
    hdf5_save(fname)
