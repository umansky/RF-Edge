import numpy as np
import matplotlib.pyplot as plt


def filter2d(var2d,x,y, x0=0.0, y0=0.0, width=1.0):

    dims=var2d.shape
    nx=dims[0]
    ny=dims[1]

    envelope=np.exp(-((x-x0)**2+(y-y0)**2)/width**2)    
    var2dnew=var2d*envelope

    return var2dnew


