import glob
from shutil import copyfile

for f in glob.glob('*smoothed'):
    print(f.replace('-smoothed', ''))
    copyfile(f.replace('-smoothed', ''), f.replace('-smoothed', '-rough'))
    copyfile(f, f.replace('-smoothed', ''))
