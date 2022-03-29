exec(open("uedge18.0.py").read())
mu.paws("Base case set")

exec(open("import_vorpal_data.py").read())
mu.paws("Vorpal data imported")


i=59
n=100
ionFrac=i/n
elFrac=i/n

bbb.pondomfpari_use[:,:,0]=-ionFrac*pondomfpari_use #-minus sign to correct the bug in UEDGE
bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.10, x0=0.30, y0=-0.45)


#fname="./tmp_e"+ "{:.3f}".format(elFrac) + "_i" + "{:.3f}".format(ionFrac) + ".h5"
#print("Restoring data from file ", fname)
fname="uedge18.1.h5"
hdf5_restore(fname)

bbb.dtreal=1e20
bbb.exmain()
