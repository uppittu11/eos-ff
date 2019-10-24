import glob
import matplotlib.pyplot  as plt
import numpy as np

plt.figure(dpi=350, figsize=(5, 5))
#filelist = glob.glob('*ester*txt')
filelist = ['ester-amide.txt', 'ester-mhead2.txt', 'ester-oh1.txt', 'ester-oh2.txt']
for f in filelist:
    dat = np.loadtxt(f)
    plt.plot(dat[:,0], dat[:,1], label=f.split('.')[0])
    dat = np.loadtxt(f+'-rough')
    plt.plot(dat[:,0], dat[:,1], label=f.split('.')[0]+'-rough')

plt.ylim(-10, 30)
plt.legend()
plt.savefig('figure.png')
