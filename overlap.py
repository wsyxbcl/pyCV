from cv import *
rootdir = 'T:/programs/python/py_CV/data/'
cv_list = cv_collect(rootdir)

pos = plt.subplots(1,1)[1]
cv_overlap = []
cv_overlap.append(cv_list[18])
cv_overlap.append(cv_list[33])
cv_overlap.append(cv_list[44])
overlap(cv_overlap, filename = 'test_cv', labels = [1,2,3], pos = pos)

plt.close()

pos = plt.subplots(1,1)[1]
cv_overlap = []
cv_overlap.append(cv_list[16])
cv_overlap.append(cv_list[17])
cv_overlap.append(cv_list[18])
overlap(cv_overlap, filename = 'test1_cv', labels = [1,2,3], pos = pos)

pos = plt.subplots(1,1)[1]
cv_overlap = []
cv_overlap.append(cv_list[1])
cv_overlap.append(cv_list[2])
overlap(cv_overlap, filename = 'test1_cv', labels = [1,2], pos = pos)