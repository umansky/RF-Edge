exec(open("uedge.16.0.py").read())
mu.paws("Base case set")

exec(open("import_vorpal_data.py").read())
mu.paws("Vorpal data imported")


i=25
n=100
ionFrac=i/n
elFrac=i/n

#-Note: minus sign to correct the bug in UEDGE
#-Note: outer wall at x=0.40 m, antenna at y=-0.45 m
bbb.pondomfpari_use[:,:,0]=-ionFrac*filter2d(pondomfpari_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.10, x0=0.45, y0=-0.45)

bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.10, x0=0.45, y0=-0.45)


#fname="./tmp_e"+ "{:.3f}".format(elFrac) + "_i" + "{:.3f}".format(ionFrac) + ".h5"
#print("Restoring data from file ", fname)
fname="uedge.16.1.h5"
hdf5_restore(fname)

bbb.dtreal=1e20
bbb.exmain()
