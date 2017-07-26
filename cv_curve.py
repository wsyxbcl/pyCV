import matplotlib.pyplot as plt

class CV:
    def __init__(self, data, info, high, low):
        self.data = data
        self.info = info
        self.high = high
        self.low = low
        
    def plot(self, saving_path, filename, cyc = 'all', labels = None, pos = None):
        '''
        cyc is a 2-dim list containing segments. e.g. [[1],[2,3]]
        '''
        if labels is None:
            labels = []
        if pos is None:
            fig, pos = plt.subplots(1,1)
        if cyc == 'all':
            self.data.plot(x = 'Potential',
                           y = 'Current',
                           xlim=[self.low, self.high],
                           title = self.info,
                           grid = True)
        else:
            for i, c in enumerate(cyc):
                pos = self.data.ix[c].plot(x = 'Potential',
                                           y = 'Current',
                                           xlim=[self.low, self.high],
                                           ax = pos,
                                           label = labels[i],
                                           title = self.info,
                                           grid = True)
            pos.set_xlabel("Potential")
            pos.set_ylabel("Current")
        plt.savefig(saving_path+filename+'.png', dpi=300)
        print(saving_path+filename+'.png'+' Saved')