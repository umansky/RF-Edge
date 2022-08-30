z=com.zm[:,0,0]

ufile="uedge17.0.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.tes[:,21]/bbb.ev, label="0")

ufile="uedge17.1.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.tes[:,21]/bbb.ev,"--", label="1")

ufile="uedge17.2.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.tes[:,21]/bbb.ev,"-.", label="2")

ufile="uedge17.3.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.tes[:,21]/bbb.ev,"-.", label="3")

ufile="uedge17.4.h5"
hdf5_restore(ufile)
plt.plot(z, bbb.tes[:,21]/bbb.ev,"-.", label="4")

plt.legend(loc="lower left")

plt.title("case nstx_nw17B_f20", loc="right")
plt.suptitle("Te along outer wall")
plt.xlabel("R [m]")
plt.ylabel("Te [eV]")

plt.show()
