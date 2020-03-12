import matplotlib.pyplot as plt
import numpy as np
import glob
from msibi.utils.smoothing import savitzky_golay

for f in glob.glob('*ester*txt'):
    print(f)

    # load potential
    dat = np.loadtxt(f)

    # get the location of the head correction
    i = 10
    while np.abs(np.abs((dat[i-1, 1] - dat[i, 1]) / (dat[i, 1] - dat[i+1, 1])) - 1) < 0.05:
        i += 1
    print(i, dat[i-1, 1] - dat[i, 1], dat[i, 1] - dat[i+1, 1])
    # get r
    r = np.copy(dat[:,0])

    # get V and smooth
    V = np.copy(dat[:,1])
    V = savitzky_golay(V, 11, 2)
    V = savitzky_golay(V, 5, 2)

    # apply head correction
    m = V[i-1] - V[i]
    for i in reversed(range(i)):
        V[i] = V[i+1] + m

    dr = r[2] - r[1]
    F = -1.0 * np.gradient(V, dr)

    smoothed = np.vstack([r, V, F])
    np.savetxt(f+'-smoothed', smoothed.T)

