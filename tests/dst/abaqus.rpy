# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by Hailin on Thu Jan 20 14:25:21 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.789474, 0.789692), 
    width=116.211, height=78.3375)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('output.py', __main__.__dict__)
#: Model: C:/Users/Hailin/OneDrive/Documents/GitHub/PyAbaqusBase/tests/dst/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       15
#: Number of Node Sets:          17
#: Number of Steps:              2
#: C:\SIMULIA\EstProducts\2021\win_b64\tools\SMApy\python2.7\lib\site-packages\numpy\core\fromnumeric.py:2920: RuntimeWarning: Mean of empty slice.
#:   out=out, **kwargs)
#* FloatingPointError: invalid value encountered in double_scalars
#* File "output.py", line 47, in <module>
#*     TIME = np.mean(np.array(CSHEAR1), axis=0)[:, 0]
#* File 
#* "C:\SIMULIA\EstProducts\2021\win_b64\tools\SMApy\python2.7\lib\site-packages\numpy\core\fromnumeric.py", 
#* line 2920, in mean
#*     out=out, **kwargs)
#* File 
#* "C:\SIMULIA\EstProducts\2021\win_b64\tools\SMApy\python2.7\lib\site-packages\numpy\core\_methods.py", 
#* line 85, in _mean
#*     ret = ret.dtype.type(ret / rcount)
