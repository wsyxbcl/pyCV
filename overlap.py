from cv import *
rootdir = 'T:/programs/python/py_CV/data/'
cv_list = cv_collect(rootdir)
import os.path
import pickle

rootdir = 'T:/programs/python/py_CV/test/'

if os.path.isfile(rootdir+'cv_data.pickle'):
    with open(rootdir+'cv_data.pickle', 'rb') as f:
        cv_list = pickle.load(f)
else:
    cv_list = cv_collect(rootdir)

# pos = plt.subplots(1,1)[1]
# cv_overlap = []
# cv_overlap.append(cycle_split(cv_list[4])[2])
# cv_overlap.append(cycle_split(cv_list[11])[2])
# cv_overlap.append(cycle_split(cv_list[18])[2])
# cv_overlap.append(cycle_split(cv_list[23])[8])
# cv_overlap.append(cycle_split(cv_list[33])[2])
# cv_overlap.append(cycle_split(cv_list[37])[2])
# cv_overlap.append(cycle_split(cv_list[42])[2])

# overlap(cv_overlap,
        # filename = 'metal_cv',
        # title = 'Different WE in TMAOH/EmimTFSI, r-Cu, c-C, 10mv/s',
        # labels = ['GC', 'Ag2O/GC', 'Pb', 'Sn', 'Cd', 'Cu', 'Zn'],
        # pos = pos)

# plt.close()

pos = plt.subplots(1,1)[1]
cv_overlap = []
cv_overlap.append(cycle_split(cv_list[4])[2])
cv_overlap.append(cycle_split(cv_list[16])[1])
cv_overlap.append(cycle_split(cv_list[22])[1])
cv_overlap.append(cycle_split(cv_list[37])[2])
cv_overlap.append(cycle_split(cv_list[41])[3])

overlap(cv_overlap,
        filename = 'metal_weird_cv',
        title = 'Different WE in TMAOH/EmimTFSI, r-Cu, c-C, 10mv/s',
        labels = ['GC', 'Pb', 'Sn', 'Cu', 'Zn'],
        pos = pos)

plt.close()

# pos = plt.subplots(1,1)[1]
# cv_overlap = []
# cv_overlap.append(cv_list[16])
# cv_overlap.append(cv_list[17])
# cv_overlap.append(cv_list[18])
# overlap(cv_overlap, filename = 'test1_cv', labels = [1,2,3], pos = pos)

# pos = plt.subplots(1,1)[1]
# cv_overlap = []
# cv_overlap.append(cv_list[1])
# cv_overlap.append(cv_list[2])
# overlap(cv_overlap, filename = 'test1_cv', labels = [1,2], pos = pos)