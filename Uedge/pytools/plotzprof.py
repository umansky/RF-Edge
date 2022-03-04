import matplotlib.pyplot as plt
from uedge import bbb, com, api


def plotzprof(var, title="UEDGE data", iy=com.ny,
              lines=True, dots=False, xlim=None, ylim=None, xlog=False, ylog=False):
    # Plotting vertical profiles of UEDGE data
    #
    # Usage example:
    # plotzprof(bbb.te/ev, title="Te [eV]")
    #==================================#
    

    fig,ax = plt.subplots(1)

    if (lines):
        plt.plot(com.zm[:,iy,0],var[:,iy])
    
    if (dots):
        plt.plot(com.zm[:,iy,0],var[:,iy],"o")

        
    if xlim:
        plt.xlim(xlim)

    if ylim:
        plt.ylim(ylim)

    if ylog:
        plt.yscale('log')

    if xlog:
        plt.xscale('log')
        
    plt.xlabel('Z [m]')
    fig.suptitle(title)
    plt.grid(True)
 
    plt.show()
