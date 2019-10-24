import shutil
import glob
import copy

files = glob.glob('*amide*')

for x in files:
    shutil.copy2(x, x.replace('amide', 'ester'))
    print(x)
