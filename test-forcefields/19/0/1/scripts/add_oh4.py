import shutil
import glob
import copy

files = glob.glob('*oh2*')

for x in files:
    shutil.copy2(x, x.replace('oh2', 'oh4'))
    print(x)
