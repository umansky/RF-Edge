#Usage:
#from import_vorpal import *
#import_vorpal(ufile="mycase_tj.h5", vfile="VorpalDataOnUedgeGrid.h5")
#=====================================================================#



import h5py
import numpy as np
import matplotlib.pyplot as plt




def import_vorpal(ufile="uedge.h5", vfile="vfile.h5"):

    #-uedge data (grid etc.)
    print("\n***Importing data from ", ufile)
    data = h5py.File(ufile, 'r')

    for group in data.keys():
        
        for dset in data[group]:
            ds_data = data[group][dset]

            if (dset == "rm" and ds_data.ndim == 3):
                print("Found 3D array rm in group", group)
                rm=ds_data[:,:,:]

            if (dset == "zm" and ds_data.ndim == 3):
                print("Found 3D array zm in group", group)
                zm=ds_data[:,:,:]

                
    #-vorpal data (ponderomotive force)
    print("\n***Importing data from ", vfile)
    data = h5py.File(vfile, 'r')
    for group in data.keys():
        dset=data[group]

        if (group == "pfEpar" and dset.ndim == 2):
            print("Found 2D array pfEpar in group", group)
            pfEpar=dset[:,:] #- adding [:] returns a 2D numpy array

        if (group == "pfIpar" and dset.ndim == 2):
            print("Found 2D array pfIpar in group", group)
            pfIpar=dset[:,:] #- adding [:] returns a 2D numpy array

        if (group == "xgrid" and dset.ndim == 2):
            print("Found 2D array xgrid in group", group)
            xgrid=dset[:,:] #- adding [:] returns a 2D numpy array

        if (group == "ygrid" and dset.ndim == 2):
            print("Found 2D array ygrid in group", group)
            ygrid=dset[:,:] #- adding [:] returns a 2D numpy array


    return rm, zm, xgrid, ygrid, pfEpar, pfIpar




rm, zm, xgrid, ygrid, pfEpar, pfIpar = import_vorpal(ufile="mycase_tj.h5", vfile="VorpalDataOnUedgeGrid.h5")

plt.plot(xgrid,ygrid,".")
plt.contour(xgrid,ygrid,pfIpar)
plt.show()

