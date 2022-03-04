#-scale down the forces, to simplify convergence
ionFrac=0.0
elFrac=0.03

print("ionFrac=",ionFrac)
print("elFrac=",elFrac)
bbb.pondomfpari_use[:,:,0]=-ionFrac*pondomfpari_use #-minus sign to correct bug in UEDGE
#bbb.pondomfpare_use[:,:]=elFrac*pondomfpare_use
bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], 
                                         width=0.3, x0=0.45, y0=-0.45)


bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
rundt(1e-8)

##hdf5_save("tmp_e0.03_i0.00.h5")
##hdf5_save("tmp_e0.04_i0.00.h5")


#plt.plot(com.zm[:,0,0], bbb.ni[:,20,0])
#plt.xlabel("Z [m]")
#plt.xlabel("Ni [m-3]")
#plt.title("Plasma density along outer wall")
#plt.show()
