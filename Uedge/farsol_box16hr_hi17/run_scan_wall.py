from runcase import *
exec(open("./run2steady.py").read())
###exec(open("make_plots.py").read())
mu.paws("Base case set")


n=10
for i in range(1,n+1):
    #
    radx=0.3+0.1*(i/n)
    grd.radx=radx

    print("Using radx=", radx)

    bbb.newgeo=1
    bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
    rundt(1e-8)

    fname="./tmp_radx"+ "{:.3f}".format(radx) + ".h5"
    print("Saving in file ", fname)

    hdf5_save(fname)
    ##plotzprof(bbb.ni[:,:,0])
