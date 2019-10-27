import shutil
import glob
import copy

files = glob.glob('*tail*')

for x in files:
    if "ctail" not in x:
        shutil.copy2(x, x.replace('tail', 'taild'))
        print(x)
