from runcase import *
###exec(open("./run2steady.py").read())
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp
from rundth import *

#-high resolution settings
com.nycore[0]=16
com.nysol[0]=32 
com.nxleg[0,1]=24 
com.nxcore[0,1]=24
bbb.allocate()

hdf5_restore("cmod_box3_hr.h5")

#-short run to initialize everything
#bbb.dtreal=1e-12
#bbb.isbcwdt=1


bbb.restart=1
bbb.exmain()

