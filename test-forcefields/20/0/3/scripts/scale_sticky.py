import numpy as np
import glob

scaling = {
        ("sticky", "oh1"): 1.5,
        ("sticky", "oh2"): 1.5,
        ("sticky", "amide"): 1.5,
        ("sticky", "head"): 1.5,
        ("sticky", "chead"): 1.5
        }
for fname in glob.glob('*sticky*txt'):
    if "step" in fname:
        continue
    pair = fname.split('.')[0].split('-')
    print(pair)
    fact = 1
    try:
        fact = scaling[(pair[0], pair[1])]
    except:
        try:
            fact = scaling[(pair[1], pair[0])]
        except:
            continue
    print("Scaling {} by {}".format(fname, fact))
    data = np.loadtxt(fname)
    data[:,1] *= fact
    data[:,2] *= fact
    np.savetxt(fname, data)
