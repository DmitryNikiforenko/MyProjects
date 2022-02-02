from sys import argv
script_mane, b = argv

from itertools import cycle
c = 0
for x in cycle(b):
    if c > 10:
        break
    else:
        print(x)
        c += 1
