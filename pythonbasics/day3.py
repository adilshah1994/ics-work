# Scripts and Libraries
# 1


# 2


# 3


# Sets and Dictionaries
# 1

a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])

print a.union(b)

print a.intersection(b)


# 2

band = ["mel", "geri", "victoria", "mel", "emma"]

counts = {}

for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

for name in counts:
    print name, counts[name]


# 3

if {}:
    print 'hi'

d = {"maggie": "uk", "ronnie": "usa"}

print dir(d)

print d.items()

print d.keys()

print d.values()

print d.get("maggie", "no country")

print d.get("major", "no country")

res = d.setdefault("mikhail", "ussr")
print res, d["mikhail"]


# Introduction to NumPy Arrays
# 1

import numpy as np

x = range(1, 11)

a1 = np.array(x, np.int64)

a2 = np.array(x, np.float64)

print a1.dtype
print a2.dtype


# 2

a = np.zeros((2, 3, 4), dtype=np.int64)

a = np.ones((2, 3, 4), dtype=np.int64)

a = np.arange(1000)


# 3

x = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
a = np.array(x)

print a[1]

print a[1:4]

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])

print a[:, 3]

print a[1:4, 0:4]

print a[1:, 2]
