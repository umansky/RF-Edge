###exec(open("./make_plots.py").read())


mp.plotrprof(bbb.te/bbb.ev, title="Midplane profile of Te [eV]", lines=True, dots=True)
plt.savefig('te_1D.pdf')

mp.plotrprof(bbb.ti/bbb.ev, title="Midplane profile of Ti [eV]", lines=True, dots=True)
plt.savefig('ti_1D.pdf')

mp.plotrprof(bbb.ni[:,:,0], title="Midplane profile of Ni [m-3]", lines=True, dots=True)
plt.savefig('ni_1D.pdf')

mp.plotrprof(bbb.ni[:,:,1], title="Midplane profile of Nn [m-3]", lines=True, dots=True)
plt.savefig('nn_1D.pdf')




mp.plotvar(bbb.te/bbb.ev, iso=False, title="Te @ steady state", label='eV', yinv=True)
plt.savefig('te_2D.pdf')                                                                                         

mp.plotvar(bbb.ti/bbb.ev, iso=False, title="Ti @ steady state", label='eV', yinv=True)
plt.savefig('ti_2D.pdf')                                                                                         

mp.plotvar(bbb.ni[:,:,0], iso=False, title="Ni @ steady state", label='m-3', yinv=True)
plt.savefig('ni_2D.pdf')                                                                                         

mp.plotvar(bbb.ni[:,:,1], iso=False, title="Nn @ steady state", label='m-3', yinv=True)
plt.savefig('nn_2D.pdf')                                                                                         

mp.plotvar(bbb.up[:,:,0], iso=False, title="Up,i @ steady state", label='m/s', yinv=True, vmax=1e4, vmin=-1e4)
plt.savefig('upi_2D.pdf')
