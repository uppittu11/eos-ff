import glob
from os import path

for f in sorted(glob.glob("*.txt")):
    basename = f.split('.')[0]
    pairs = basename.split("-")
    assert path.exists("{}-{}.txt".format(*pairs))
    if path.exists("{}-{}.txt".format(*reversed(pairs))) and pairs[0] != pairs[1]:
        print(pairs)

