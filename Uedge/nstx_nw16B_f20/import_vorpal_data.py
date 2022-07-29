##-insert directory ../pytools in the Python path
cwd=os.getcwd()
os.chdir('./../pytools')
pwd_pytools=os.getcwd()
sys.path.insert(1, pwd_pytools)
os.chdir(cwd)


#-import scripts from ../pytools
from import_vorpal import *
from filter2d import *


###vfile="vorpal17.0.h5"
xgrid,ygrid,pondomfpare_use,pondomfpari_use=ImportVorpal(vfile=vfile)

mp.plotvar(pondomfpare_use, title="Electron Fpar from Vorpal (raw, as is in the file)", \
           iso=False, label="N/m^3")
mp.plotvar(pondomfpari_use, title="Ion Fpar from Vorpal (raw, as is in the file)", \
           iso=False, label="N/m^3")

#-applying scaling factor (equal 1.0 if scaling is already in Vorpal data)
pondomfpare_use = pondomfpare_use*elFrac
pondomfpari_use = pondomfpari_use*ionFrac


#mp.plotvar(pondomfpare_use, title="Electron Fpar from Vorpal (w/ scaling factor)", \
#           iso=False, vmax=3e-2/elFrac, vmin=-3e-2/elFrac, label="N/m^3")
#mp.plotvar(pondomfpari_use, title="Ion Fpar from Vorpal (w/ scaling factor)", \
#           iso=False, vmax=3e-2/ionFrac, vmin=-3e-2/ionFrac, label="N/m^3")
