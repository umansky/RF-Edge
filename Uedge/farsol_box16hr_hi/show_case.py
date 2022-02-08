from runcase import *
exec(open("./run2steady.py").read())
exec(open("vorpal2uedge.py").read())
from filter2d import *
mu.paws()


#-scale down the forces, to simplify convergence
bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*0.0
bbb.pondomfpare_use[:,:]=1e-1*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], width=0.1, x0=0.45, y0=-0.45)
#mp.plotvar(bbb.pondomfpare_use,iso=False, vmax=1e-4,vmin=-1e-4)

i=3
ionFrac=0.0
elFrac=i/10.
print("ionFrac=",ionFrac)
print("elFrac=",elFrac)

    
bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*ionFrac
bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], width=0.1, x0=0.45, y0=-0.45)

fname="./mtmp_e"+ "{:.3f}".format(elFrac) +"_e0.0.h5"
print("Restoring file ", fname)

hdf5_restore(fname)
bbb.exmain()
