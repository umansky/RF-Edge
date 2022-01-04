#from runcase import *
from vorpal2uedge import *


ifile='./ion_data.h5'
efile='./electron_data.h5'
##uefile="tmp_i1.000_e0.0.h5"


Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=ifile)
#val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
#pondomfpari_use=np.nan_to_num(val)
plt.contourf(Xgrid,Ygrid,Fparallel,10)                                                                         
plt.title("Vorpal ion parallel ponderomotive force [N/m^3]")                                              
plt.xlabel("X [m]")                                                                                            
plt.ylabel("Y [m]")                                                                                            
plt.colorbar()                                                                                                 
plt.show()      


Xgrid, Ygrid, Fparallel = ImportVorpal(vfile=efile)
#val=Vorpal2uedge(Xgrid, Ygrid, Fparallel, com.rm, com.zm, debug=False)
plt.contourf(Xgrid,Ygrid,Fparallel,10)                                                                         
plt.title("Vorpal electron parallel ponderomotive force [N/m^3]")                                              
plt.xlabel("X [m]")                                                                                            
plt.ylabel("Y [m]")                                                                                            
plt.colorbar()                                                                                                 
plt.show()      
