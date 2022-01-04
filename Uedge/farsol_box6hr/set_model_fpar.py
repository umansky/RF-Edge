#Usage:
#from set_model_fpar import *
#set_model_fpar(iscale=1e-6, escale=0.0)
#mp.plotvar(bbb.pondomfpari_use[:,:,0])
#==================================================#

import numpy as np
from uedge import bbb, com


def set_model_fpar(iscale=1.0, escale=1.0):

    pondomfpari_use=np.sin(com.zm[:,:,0]*5)*np.exp(-30*com.zm[:,:,0]**2)*\
                     np.exp(-10*(com.rm[:,:,0]-np.max(com.rm[:,:,0]))**2)
    pondomfpari_use=pondomfpari_use/np.max(pondomfpari_use)
    pondomfpare_use=pondomfpari_use


    bbb.pondomfpari_use[:,:,0]=iscale*pondomfpari_use
    bbb.pondomfpare_use[:,:]=escale*pondomfpare_use
