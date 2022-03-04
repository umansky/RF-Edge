import numpy as np
import matplotlib.pyplot as plt


def filter2d(var2d,x,y, x0=0.0, y0=0.0, width=1.0, option=0):

    dims=var2d.shape
    nx=dims[0]
    ny=dims[1]

    dist=np.sqrt((x-x0)**2+(y-y0)**2)

    if (option==0):
        envelope=np.zeros((nx,ny))
        ii=np.where(dist<width)
        envelope[ii]=1.0
    elif (option==1):
        envelope=np.exp(-((x-x0)**2+(y-y0)**2)/width**2)    

    #-scale input variable by the envelope
    var2dnew=var2d*envelope

    return var2dnew
