#exec(open("run_scan_difni.py").read())

from runcase import *
exec(open("./run2steady.py").read())
bbb.dtreal=1e20; bbb.exmain()
mu.paws("Restored the base case")


i=500
bbb.difni[0]=2.5 + i*0.001
fname="./tmp_difni_"+ "{:.6f}".format(bbb.difni[0]) +".h5"
print("Restoring ", fname)
hdf5_restore(fname)
bbb.dtreal=1e20; bbb.exmain()
