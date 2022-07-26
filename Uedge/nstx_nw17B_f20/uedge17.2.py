exec(open("uedge17.0.py").read())
mu.paws("Base case set")


vfile="vorpal17.1.h5"
elFrac=1.00 #-for this case, scaling applied in Vorpal, not doing it in import_vorpal()
ionFrac=1.00
exec(open("import_vorpal_data.py").read())



#-Note: minus sign to correct the bug in UEDGE
#-Note: outer wall at x=0.40 m, antenna at y=-0.45 m
bbb.pondomfpari_use[:,:,0]=-filter2d(pondomfpari_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.10, x0=0.40, y0=-0.45)

bbb.pondomfpare_use[:,:]=filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.10, x0=0.40, y0=-0.45)

print("Using filtering and scaling (e/i):", elFrac, ionFrac)
mu.paws("Vorpal data imported")


fname="uedge17.2.h5"
hdf5_restore(fname)
bbb.dtreal=1e20
bbb.exmain()
