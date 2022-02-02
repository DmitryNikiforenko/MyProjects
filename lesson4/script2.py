from sys import argv
script_name, a = argv
a = int(a)
from itertools import count
print([print(x) for x in count(a) if x < a + 11])
