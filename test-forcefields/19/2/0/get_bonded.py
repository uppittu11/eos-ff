import pickle
import sys

filename = sys.argv[1]

with open(filename, 'rb') as f:
   data = pickle.load(f)

print("Bonded Parameters from file:\n{}\n".format(filename))

line_len = 25

print("Bond                      r0       k")
for key in data['bonds'].keys():
   item=str(key)
   item+=" "*(25-len(item))
   r0="{0:.3f}".format(data['bonds'][key][0])
   r0+=" "*(8-len(r0))
   k="{0:.3f}".format(data['bonds'][key][1])
   print("{} {} {}".format(item, r0, k))

print(" ")

print("Angle                     t0       k")
for key in data['angles'].keys():
   item=str(key)
   item+=" "*(25-len(item))
   r0="{0:.3f}".format(data['angles'][key][0])
   r0+=" "*(8-len(r0))
   k="{0:.3f}".format(data['angles'][key][1])
   print("{} {} {}".format(item, r0, k))

