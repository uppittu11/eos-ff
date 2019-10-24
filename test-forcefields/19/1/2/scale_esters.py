import numpy as np
import glob

scaling = {
        ("ester", "mhead"): 0.50,
        ("ester", "oh1"): 0.50,
        ("ester", "oh2"): 0.50,
        ("ester", "amide"): 0.50,
        ("ester", "head"): 0.50,
        ("ester", "chead"): 0.50,
        }
for fname in glob.glob('*ester*txt'):
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
