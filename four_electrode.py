import re
from pathlib import Path

import matplotlib.pyplot as plt

from cv import *
from dir_walker import walker

rootdir = Path('./demo/four_electrode')
for filename, subdir in walker(rootdir, re.compile('cv(.*?)txt')):
    fig, (pos1, pos2) = plt.subplots(2, 1, constrained_layout=True)
    cv = txt_to_CV(Path(subdir).joinpath(Path(filename)), info=filename[:-4])

    for i, cv_cycle in enumerate(cycle_split(cv)):
        cv_cycle.plot(labels='cycle ' + str(i + 1), pos=pos1, title='disc electrode', xlabel=None)
    cv = txt_to_CV(Path(subdir).joinpath(Path(filename)), info=filename[:-4], WE2=1)

    for i, cv_cycle in enumerate(cycle_split(cv)):
        cv_cycle.plot(labels='cycle ' + str(i + 1), pos=pos2, title='ring electrode', xlabel='Potential v.s. SCE/V')
    fig.suptitle(cv_cycle.info, fontsize=16)

    fig.align_labels()
    plt.savefig(Path(subdir).joinpath(str(cv)+'.png'), dpi=300, bbox_inches='tight') # matploblib now has PathLike support
    print(str(Path(subdir).joinpath(str(cv)+'.png'))+' Saved')
