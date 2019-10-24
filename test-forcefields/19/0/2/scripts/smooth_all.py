import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
import glob

from msibi.utils.smoothing import savitzky_golay
import shutil
import os

def smooth(filename):
    print("Smoothing {}".format(filename))
    dat = np.loadtxt(filename)
    smoothed = np.copy(dat)
    smoothed[:,1] = savitzky_golay(smoothed[:,1], 11, 2)
    smoothed[:,1] = savitzky_golay(smoothed[:,1], 5, 2)
    smoothed[:,2] = savitzky_golay(smoothed[:,2], 11, 2)
    smoothed[:,2] = savitzky_golay(smoothed[:,2], 5, 2)

    if not os.path.isfile("{}-rough".format(filename)):
        shutil.copyfile(filename, "{}-rough".format(filename))
        np.savetxt(filename, smoothed)
    else:
        dat2 = np.loadtxt("{}-rough".format(filename))
        plt.plot(dat[:,0], dat[:,1], 'r')
        plt.plot(dat2[:,0], dat2[:,1], 'k')
        plt.title('{}'.format(filename))
        plt.ylim([np.min(dat2[:,1])-1, np.max([np.min(dat2[:,1])+5, 5])])
        plt.show()

filelist = ["ester-mhead2.txt",
            "ester-amide.txt",
            "ester-oh1.txt",
            "ester-oh2.txt",
            "tail-ester.txt",
            "ter2-ester.txt",
            "ester-chead.txt",
            "ester-ring.txt",
            "ester-chme.txt",
            "ester-ctail.txt",
            "ester-cterm.txt",
            "ester-head.txt",
            "ester-water.txt"]

for fname in filelist:
   smooth(fname)

