from runcase import *
###exec(open("./run2steady.py").read())
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp
from uedge.rundt import *



#-short run to initialize everything
bbb.ftol=1e8; bbb.exmain()
bbb.ftol=1e-8

#-set up some initial state
bbb.ngs=1e14; bbb.ng=1e14
bbb.nis=1e20; bbb.ni=1e20 
bbb.ups=0.0;  bbb.up=0.0
bbb.tes=bbb.ev;   bbb.te=bbb.ev
bbb.tis=bbb.ev;   bbb.ti=bbb.ev

hdf5_restore("farsol_box6hr.h5")

#-run to steady state
bbb.restart=1; bbb.ftol=1e-8; 
#bbb.isbcwdt=1
#bbb.dtreal = 1e-14; bbb.itermx=30; bbb.exmain()
#bbb.t_stop=1e0
#bbb.rundt()
###rundt(1e-8)
bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()
#hdf5_save('mycase.h5')
