##-insert directory ../pytools in the Python path
cwd=os.getcwd()
os.chdir('./../pytools')
pwd_pytools=os.getcwd()
sys.path.insert(1, pwd_pytools)
os.chdir(cwd)

#-import scripts from ../pytools
from filter2d import *
from import_vorpal import *

#vfile="VorpalDataOnUedgeGrid.h5"
#vfile="VorpalDataOnUedgeGrid.nonuniform007.h5"
vfile="vorpal18.0.h5"
xgrid,ygrid,pondomfpare_use,pondomfpari_use=ImportVorpal(vfile=vfile)


#-scale the forces if needed
ionFrac=1.0
elFrac=1.0
print("ionFrac=",ionFrac)
print("elFrac=",elFrac)


bbb.pondomfpari_use[:,:,0]=-pondomfpari_use*ionFrac
bbb.pondomfpare_use = pondomfpare_use*elFrac

##-do we need filtering at all?
#bbb.pondomfpare_use[:,:]=elFrac*filter2d(pondomfpare_use, com.rm[:,:,0], com.zm[:,:,0], width=0.1, x0=0.45, y0=-0.45)


mp.plotvar(bbb.pondomfpare_use, title="Electron Fpar from Vorpal", iso=False, vmax=3, vmin=-3)
mp.plotvar(bbb.pondomfpari_use[:,:,0], title="Ion Fpar from Vorpal", iso=False, vmax=1, vmin=-1)
