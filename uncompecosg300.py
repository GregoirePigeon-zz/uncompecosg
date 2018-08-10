#uncompecosg300.py
#programm that will call the uncompecosg300.F90 routine

import uncompecosg300 as unzeco

filein = '/home/gpigeon/Data/ECOCLIMAP_SG/test/LAI_A_0105_c.dir'
fileout = '/home/gpigeon/Data/ECOCLIMAP_SG/test/LAI_A_0105.dir'

unzeco.uncompecosg300(filein, fileout)
