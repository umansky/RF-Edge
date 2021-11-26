import h5py
import numpy as np
import matplotlib.pyplot as plt
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp




def ImportVorpal(vfile="ion_data.h5"):

    #-vorpal data (ponderomotive force)                                                                                        
    print("\n***Importing data from ", vfile)
    data = h5py.File(vfile, 'r')
    for group in data.keys():
        dset=data[group]


        if (group == "Fparallel" and dset.ndim == 2):
            print("Found 2D array Fparallel in group", group)
            Fparallel=dset[:,:] #- adding [:] returns a 2D numpy array                                                         

        if (group == "Xgrid" and dset.ndim == 2):
            print("Found 2D array Xgrid in group", group)
            Xgrid=dset[:,:] #- adding [:] returns a 2D numpy array                                                             

        if (group == "Ygrid" and dset.ndim == 2):
            print("Found 2D array Ygrid in group", group)
            Ygrid=dset[:,:] #- adding [:] returns a 2D numpy array                                                             


    return Xgrid, Ygrid, Fparallel




def Vorpal2uedge(xgrid, ygrid, vgrid, rm, zm, debug=False):
    #-map Vorpal data (xgrid,ygrid,vgrid) to UEDGE grid (rm,zm)

    #-UEDGE grid dimensions (0:nx+1,0:ny+1)
    dims=com.rm.shape    
    nx=dims[0]-2
    ny=dims[1]-2
    print("UEDGE grid dimensions:", nx,ny)


    val=np.zeros((nx+2,ny+2))

    
    if debug:
        #plt.plot(rm[:,:,0],zm[:,:,0],'.', color="black")
        for i in range(0,nx+2):
            for j in range(0,ny+2):
                #plt.plot(rm[i,j,0],zm[i,j,0])
                indx=[1,3,4,2,1]
                plt.plot(rm[i,j,indx],zm[i,j,indx], color="black")

        plt.plot(xgrid,ygrid,".",color="red")
        plt.show()
    

    #-only inner cells
    for i in range(1,nx+1):
        for j in range(1,ny+1):
            
            indx=[1,3,4,2,1]                
            plt.plot(rm[i,j,indx],zm[i,j,indx], color="black")
            #print("rm:", rm[i,j,indx])
            #print("zm:", zm[i,j,indx])

            rm_min=rm[i,j,1]
            rm_max=rm[i,j,3]
            zm_min=zm[i,j,1]
            zm_max=zm[i,j,4]
            
            #print("rm boundaries:", rm_min, rm_max)
            #print("zm boundaries:", zm_min, zm_max) 
            #mu.paws()

            #-select Vorpal data points that lie inside this UEDGE grid cell
            ind=np.where((xgrid>=rm_min) & (xgrid<=rm_max) & (ygrid>zm_min) & (ygrid<zm_max))
            #ind = np.where(xgrid>rm_min && xgrid<rm_max && ygrid<zm_max && ygrid>zm_min)
            #print("ind=", ind)
            #print("ind.shape=", ind.shape)
            #print("ind.size=", ind.size)
            #print("len(ind)=", len(ind))
            
            #print("ind[0]=", ind[0])
            #print("ind[1]=", ind[1])

            #print("len(ind[0])=", len(ind[0]))
            #print("len(ind[1])=", len(ind[1]))
            
            plt.plot(xgrid[ind],ygrid[ind],".", color="red")

            ninside=len(ind[0])
            
            if (ninside==0):
                x_ave=0.0
                y_ave=0.0
                v_ave=0.0
            else:
                x_ave=sum(xgrid[ind])/ninside
                y_ave=sum(ygrid[ind])/ninside
                v_ave=sum(vgrid[ind])/ninside

                #print("ninside=", ninside)
                #print("xgrid[ind]=", xgrid[ind])
                #print("ygrid[ind]=", ygrid[ind])
                #print("x_ave=", x_ave)
                #print("y_ave=", y_ave)
                
                plt.plot(x_ave,y_ave, "x", color="green")

            val[i,j]=v_ave
                
            #plt.show()
            #mu.paws()

    plt.show()
    return val


#-import Vorpal data    
vfile="/Users/umansky1/Projects/RFEDGE/RF-Edge.22nov2021/Uedge/JenkinsData/ion_data.h5"
Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=vfile)
val=Vorpal2uedge(Xgrid+0.4, Ygrid, Fparallel, com.rm, com.zm, debug=False)
mp.plotvar(val, title="Ion Fpar from Vorpal")


vfile="/Users/umansky1/Projects/RFEDGE/RF-Edge.22nov2021/Uedge/JenkinsData/electron_data.h5"
Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=vfile)
val=Vorpal2uedge(Xgrid+0.4, Ygrid, Fparallel, com.rm, com.zm, debug=False)
mp.plotvar(val, title="Electron Fpar from Vorpal")
