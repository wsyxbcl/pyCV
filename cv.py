import re
import os
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
from pandas import DataFrame

from dir_walker import walker


class CV:
    def __init__(self, info, data, low, high, segments):
        self.info = info
        self.data = data
        self.low = low
        self.high = high
        self.segments = segments

    def plot(self, *, labels=None, title=None, xlim=None, pos=plt.subplots(1, 1)[1], xlabel="Potential", ylabel="Current/A"):
        if xlim is None:
            xlim = [self.low, self.high]
        if title is None:
            title = self.info
        pos = self.data.plot(x='Potential',
                             y='Current',
                             xlim=xlim,
                             ax=pos,
                             label=labels,
                             title=title,
                             grid=True)
        pos.set_xlabel(xlabel)
        pos.set_ylabel(ylabel)

    def save(self, filename, path=Path(os.getcwd())):
        header = ['Potential', 'Current']
        self.data.to_csv(path.joinpath(filename+'.csv'),
                         index=False,
                         header=False,
                         columns=header)
        print("Saved to "+str(path.joinpath(filename+'.csv')))

    def __str__(self):
        return self.info+' '+str(self.low)+' to '+str(self.high)


def find_segments(data):
    num_seg = 1
    seg_label = []
    seg_label.append(num_seg)
    for i, p in enumerate(data['Potential']):
        seg_label.append(num_seg)
        if i + 2 == len(data) - 1:
            break
        delta_1 = data['Potential'][i + 1] - p
        delta_2 = data['Potential'][i + 2] - data['Potential'][i + 1]
        if delta_1 * delta_2 < 0:
            num_seg += 1
    seg_label.append(num_seg)
    # data_seg = DataFrame(data, index = [seg_label, list(range(len(data)))])
    return [num_seg, seg_label]


def txt_to_CV(file, info='CV test', WE2=0):
    """
    WE2: Sometimes there're 2 working electrodes, set WE2 to 1 if you
    want to use current collected from WE2 channel. 
    """
    h = 0
    l = 0
    record = 0
    a = []
    with open(file, 'rt') as f:
        print(str(file)+' Opened')
        for line in f:
            if not (h and l):
                if line.startswith('High'):
                    high = float(re.split(', |,| |\t', line)[4])
                    h = 1
                if line.startswith('Low'):
                    low = float(re.split(', |,| |\t', line)[4])
                    l = 1
            if record:
                a.append(line)
            if line.startswith("Potential"):
                record = 1
    current = []
    potential = []
    for i in a[1:]:
        if WE2:
            current.append(float(re.split(', |,| |\t', i)[2]))
        else:
            current.append(float(re.split(', |,| |\t', i)[1]))
        potential.append(float(re.split(', |,| |\t', i)[0]))
    data = {"Potential": potential, "Current": current}
    frame = DataFrame(data)
    [num_seg, seg_label] = find_segments(frame)
    frame.index = seg_label
    return CV(info, frame, low, high, list(range(1, num_seg + 1)))


def cycle_split(cv):
    '''
    Used to extract single cycle from CV curve to form a list
    '''

    def seg_to_cyc(num_seg):
        if num_seg % 2:
            cycle_all = [[1]]
            for i in list(range(2, num_seg + 1, 2)):
                cycle_all.append([i, i + 1])
        else:
            cycle_all = []
            for i in list(range(1, num_seg + 1, 2)):
                cycle_all.append([i, i + 1])
        return cycle_all

    cv_cycles = []
    cycles = seg_to_cyc(len(cv.segments))
    for i in cycles:
        cv_cycles.append(CV(cv.info, cv.data.ix[i], cv.low, cv.high, i))
    return cv_cycles


def overlap(cv_list, *, path='.', filename='cv_overlap', title='No title', pos=plt.subplots(1, 1)[1], labels=None):
    '''
    Overlap CV_curve in given list
    '''
    l = []
    h = []
    if labels is None:
        labels = []
        for cv in cv_list:
            labels.append(str(cv))
    for cv in cv_list:
        l.append(cv.low)
        h.append(cv.high)
    low = min(l)
    high = max(h)
    for i, cv in enumerate(cv_list):
        # pos = cv.data.plot(x = 'Potential',
        # y = 'Current',
        # xlim = [low, high],
        # ax = pos,
        # label = labels,
        # title = title,
        # grid = True)
        cv.plot(labels=labels[i], title=title, xlim=[low, high], pos=pos)
    pos.set_xlabel('Potential')
    pos.set_ylabel('Current')
    plt.savefig(path.joinpath(filename), dpi=300, bbox_inches='tight')


def cv_collect(rootdir):
    cv_list = []
    for filename, subdir in walker(rootdir, re.compile('cv(.*?)txt')):
        cv_list.append(txt_to_CV(Path(subdir).joinpath(filename), filename[:len(filename) - 4]))
    with open(rootdir.joinpath('list_cv.txt'), 'w') as f:
        f.truncate()
        for i, cv in enumerate(cv_list):
            f.write(str(i)+' '+cv.info)
            f.write('\n')
    print()
    print('List of CV has been saved to '+str(rootdir)+'cv_list.txt')
    with open(rootdir.joinpath('data_cv.pickle'), 'wb') as f:
        pickle.dump(cv_list, f, pickle.HIGHEST_PROTOCOL)
    print()
    print("CV information has been dumped to "+str(rootdir)+'cv_data.pickle')
    return cv_list

__all__ = ['CV', 'find_segments', 'cycle_split', 'txt_to_CV', 'cv_collect', 'overlap']

if __name__ == '__main__':
    rootdir = Path('./demo')
    for filename, subdir in walker(rootdir, re.compile('cv(.*?)txt')):
        fig, pos = plt.subplots(1, 1)
        cv = txt_to_CV(Path(subdir).joinpath(Path(filename)), info=filename[:-4])
        for i, cv_cycle in enumerate(cycle_split(cv)):
            cv_cycle.plot(labels='cycle ' + str(i + 1), pos=pos)
        plt.savefig(Path(subdir).joinpath(str(cv)+'.png'), dpi=300, bbox_inches='tight') # matploblib now has PathLike support
        print(str(Path(subdir).joinpath(str(cv)+'.png'))+' Saved')
