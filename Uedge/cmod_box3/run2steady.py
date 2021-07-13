from runcase import *
###exec(open("./run2steady.py").read())
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp


#-short run to initialize everything
bbb.ftol=1e8; bbb.exmain()
bbb.ftol=1e-8

#-set up some initial state
bbb.ngs=1e14; bbb.ng=1e14
bbb.nis=1e20; bbb.ni=1e20 
bbb.ups=0.0;  bbb.up=0.0
bbb.tes=bbb.ev;   bbb.te=bbb.ev
bbb.tis=bbb.ev;   bbb.ti=bbb.ev

#hdf5_restore("mycase3.h5")

#-run to steady state
bbb.restart=1; bbb.ftol=1e-8; 
bbb.isbcwdt=1
bbb.dtreal = 1e-14; bbb.itermx=30; bbb.exmain()
bbb.t_stop=1e0
bbb.rundt()
bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()
hdf5_save('mycase.h5')

plt.ion()

mp.plotvar(bbb.te/bbb.ev, iso=False, title="Te @ steady state", label='eV', yinv=True)
plt.savefig('te.pdf')

mp.plotvar(bbb.ni[:,:,0], iso=False, title="Ni @ steady state", label='m-3', yinv=True)
plt.savefig('ni.pdf')

mp.plotvar(bbb.ni[:,:,1], iso=False, title="Nn @ steady state", label='m-3', yinv=True)
plt.savefig('nn.pdf')

mp.plotvar(bbb.up[:,:,0], iso=False, title="Up @ steady state", label='m/s', yinv=True)
plt.savefig('up.pdf')
