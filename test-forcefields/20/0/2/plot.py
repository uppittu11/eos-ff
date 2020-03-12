import glob
import matplotlib.pyplot  as plt
import numpy as np

plt.figure(dpi=350, figsize=(5, 5))
#filelist = glob.glob('*ester*txt')
filelist = ["ester-ester.txt", "tail-ester.txt", "taild-oh1.txt"]
#filelist = ['ester-chead.txt', 'ester-ring.txt', 'ester-chme.txt', 'ester-ctail.txt', 'ester-cterm.txt']
for f in filelist:
    dat = np.loadtxt(f)
    plt.plot(dat[:,0], dat[:,1], label=f.split('.')[0])

plt.ylim(-10, 30)
#plt.legend()
plt.savefig('figure.png')
