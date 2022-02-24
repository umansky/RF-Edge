mp.plotmesh(iso=True)
mp.plotmesh(iso=True, xlim=[0.0,0.5], ylim=[-0.7,-0.2])

mp.plotvar(bbb.te/bbb.ev, iso=False, title="Te", label="eV")
mp.plotvar(bbb.ni[:,:,0], iso=False, title="Ni", label="m-3")
mp.plotvar(bbb.ni[:,:,1], iso=False, title="Nn", label="m-3", vmax=1e19)

mp.plotrprof(bbb.te/bbb.ev, title="Midplane radial profile: Te [eV]")
mp.plotrprof(bbb.ni[:,:,0], title="Midplane radial profile: Ni [m-3]")
mp.plotrprof(bbb.ni[:,:,0], title="Midplane radial profile: Ni [m-3]", ylog=True)
mp.plotrprof(bbb.ni[:,:,1], title="Midplane radial profile: Nn [m-3]")
