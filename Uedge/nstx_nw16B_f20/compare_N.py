z=com.zm[:,0,0]

ufile="uedge16.0.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.nis[:,21,0], label="0")

ufile="uedge16.1.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.nis[:,21,0],"--", label="1")

#ufile="uedge18.2.h5"
#hdf5_restore(ufile)
#plt.plot(z, bbb.nis[:,21,0],"-.", label="2")

plt.legend(loc="lower left")

plt.title("case nstx_nw16B_f20", loc="right")
plt.suptitle("Ni along outer wall")
plt.xlabel("R [m]")
plt.ylabel("Ni [m-3]")

plt.show()
