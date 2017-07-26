from cv_curve import CV
from cv_seg import find_segments
from cv_seg import seg_to_cyc
from cv_seg import label_maker
import os
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

# ls = glob.glob("*.txt")
rootdir = 'T:/programs/python/py_CV/data/'
ls_filename = []
ls_subdirs = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('txt') and file.startswith('cv'):
            ls_filename.append(file)
            ls_subdirs.append(subdir)

# read in .txt file, and data should be seperated with tab            
for filename, subdir in zip(ls_filename, ls_subdirs):
    h = 0
    l = 0
    record = 0
    a = []
    with open(subdir+'/'+filename, 'rt') as f:
        print(subdir+'/'+filename+' Opened')
        for line in f:
            if not (h and l):
                if line.startswith('High'):
                    high = float(line.split()[4])
                    h = 1
                if line.startswith('Low'):
                    low = float(line.split()[4])
                    l = 1
            if record:
                a.append(line)
            if line.startswith("Potential"):
                record = 1
    current = []
    potential = []
    for i in a[1:]:
        current.append(float(i.split()[1]))
        potential.append(float(i.split()[0]))
    cv_data = {"Potential": potential, "Current": current}
    frame = DataFrame(cv_data)
    cv_info = filename[:len(filename) - 4] # *.txt
    cv_curve = CV(frame, cv_info, high, low)
    #seg_label = cv_curve.get_segments()
    [seg_num, seg_label] = find_segments(cv_curve.data)
    cv_curve.data.index = seg_label
    cycles = seg_to_cyc(seg_num)
    labels = label_maker('cycle', seg_num)
    # cycle_choose = [1,3]
    cycle_choose = list(range(len(cycles)))
    seg_info = 'seg'
    for i in cycle_choose:
        seg_info = seg_info + str(cycles[i])
    saving_path = subdir+'/'
    filename_pic = cv_info+' '+str(low)+'to'+str(high)+' '+seg_info    
    cv_curve.plot(saving_path, 
                  filename_pic,
                  [cycles[i] for i in cycle_choose], [labels[i] for i in cycle_choose])