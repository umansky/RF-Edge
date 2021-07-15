from runcase import *
###exec(open("./run2steady.py").read())
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp
from rundth import *

#-high resolution settings
com.nycore[0]=32
com.nysol[0]=64
com.nxleg[0,1]=48 
com.nxcore[0,1]=48
bbb.allocate()

hdf5_restore("cmod_box3_hhr.h5")

#-short run to initialize everything
#bbb.dtreal=1e-12
#bbb.isbcwdt=1


bbb.restart=1
bbb.exmain()

