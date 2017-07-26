import matplotlib.pyplot as plt
from pandas import DataFrame
from dir_walker import walker
import re

class CV:
    def __init__(self, info, data, low, high, segments):
        self.info = info
        self.data = data
        self.low = low
        self.high = high
        self.segments = segments
    
    def plot(self, label, pos):
        pos = self.data.plot(x = 'Potential',
                             y = 'Current',
                             xlim = [self.low, self.high],
                             ax = pos,
                             label = label,
                             title = self.info,
                             grid = True)
        pos.set_xlabel('Potential')
        pos.set_ylabel('Current')
        
    def save(self, filename, path):
        self.data.to_csv(path+filename+'.csv',
                         index = False,
                         header = False,
                         cols = ['Potential', 'Current'])
    
    def full_info(self):
        return self.info+' '+str(self.low)+'to'+str(self.high)+' '+str(self.segments)

        
def find_segments(data):
    num_seg = 1
    seg_label = []
    seg_label.append(num_seg)
    for i, p in enumerate(data['Potential']):
        seg_label.append(num_seg)
        if i + 2 == len(data) - 1:
            break
        delta_1 = data['Potential'][i+1] - p
        delta_2 = data['Potential'][i+2] - data['Potential'][i+1]
        if delta_1 * delta_2 < 0:
            num_seg += 1
    seg_label.append(num_seg)
    # data_seg = DataFrame(data, index = [seg_label, list(range(len(data)))])
    return [num_seg, seg_label]
    
def txt_to_CV(file, info = 'CV test'):
    h = 0
    l = 0
    record = 0
    a = []
    with open(file, 'rt') as f:
        print(file+' Opened')
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
    data = {"Potential": potential, "Current": current}
    frame = DataFrame(data)
    # cv_info = filename[:len(filename) - 4] # *.txt
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
    
if __name__ == '__main__':
    rootdir = 'T:/programs/python/py_CV/data/'
    for filename, subdir in walker(rootdir, re.compile('cv(.*?)txt')):
        fig, pos = plt.subplots(1,1)
        cv = txt_to_CV(subdir+'/'+filename, filename[:len(filename) - 4])
        for i, cv_cycle in enumerate(cycle_split(cv)):
            cv_cycle.plot('cycle '+str(i + 1), pos)
        plt.savefig(subdir+'/'+cv.full_info()+'.png', dpi=300)
        print(subdir+'/'+cv.full_info()+'.png'+' Saved')