import h5py
import numpy as np
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp




def ImportVorpal(vfile="VorpalDataOnUedgeGrid.h5"):

    #-vorpal data (ponderomotive force)                                                                                        
    print("\n***Importing data from ", vfile)
    data = h5py.File(vfile, 'r')

    for group in data.keys():
        dset=data[group]
        
        if (group == "pfEpar" and dset.ndim == 2):
            print("Found 2D array in group", group)
            fpare=dset[:,:] #- adding [:] returns a 2D numpy array
        if (group == "pfIpar" and dset.ndim == 2):
            print("Found 2D array in group", group)
            fpari=dset[:,:] #- adding [:] returns a 2D numpy array                            
                             
        if (group == "xgrid" and dset.ndim == 2):
            print("Found 2D array in group", group)
            xgrid=dset[:,:] #- adding [:] returns a 2D numpy array                            
                                 
        if (group == "ygrid" and dset.ndim == 2):
            print("Found 2D array in group", group)
            ygrid=dset[:,:] #- adding [:] returns a 2D numpy array                            
                                 
    ###print("...done")

    return xgrid, ygrid, fpare, fpari
