import os.path
import pickle
from pathlib import Path

import matplotlib.pyplot as plt

from cv import *

rootdir = Path('C:/code/pyCV/demo/overlap')
cv_list = cv_collect(rootdir)

# if os.path.isfile(rootdir.joinpath('cv_data.pickle')):
with open(rootdir.joinpath('data_cv.pickle'), 'rb') as f:
    cv_list = pickle.load(f)
# else:
# cv_list = cv_collect(rootdir)

pos = plt.subplots(1,1)[1]
cv_overlap = []
cv_overlap.append(cycle_split(cv_list[4])[2])
cv_overlap.append(cycle_split(cv_list[16])[1])
cv_overlap.append(cycle_split(cv_list[22])[1])
cv_overlap.append(cycle_split(cv_list[37])[2])
cv_overlap.append(cycle_split(cv_list[41])[3])

overlap(cv_overlap,
        path=rootdir,
        filename = 'metal_weird_cv.png',
        title = 'Different WE in TMAOH/EmimTFSI, r-Cu, c-C, 10mv/s',
        labels = ['GC', 'Pb', 'Sn', 'Cu', 'Zn'],
        pos = pos)

plt.close()
