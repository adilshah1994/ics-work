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


# Interrogating and manipulating arrays
# 1

arr = np.array([range(4), range(10,14)])

print np.shape(arr)

print np.size(arr)

print arr.max()

print arr.min()


# 2

print np.reshape(arr, (2, 2, 2))

print np.transpose(arr)

print np.ravel(arr)

print arr.astype(np.float32)


# Array calculations and operations
# 1

a = np.array([range(4), range(10,14)])

b = np.array([2, -1, 1, 0])

print a * b

b1 = b * 100
b2 = b*100.0

print b1, b2

print b1 == b2

print b1.dtype, b2.dtype


# 2

arr = np.array(range(0, 10))
print arr

print np.less(arr, 3)
print arr < 3

condition = np.logical_or(arr < 3, arr > 8)

a = np.where(condition, arr * 5, arr * -5)

print a


# Working with missing values
# 1

import numpy.ma as MA

a = MA.masked_array(range(0, 10), fill_value = -999)

print a, a.fill_value

a[2] = MA.masked

print a

print a.mask

narr = MA.masked_where(a > 7, a)

print narr.fill_value

print narr

cod = MA.filled(narr)
print cod
print type(cod)


#2

m1 = MA.masked_array(range(1, 9))
print m1

m2 = m1.reshape(2, 4)
print m2

m3 = MA.masked_greater(m2, 6)
print m3

print m3 * 100

haddock = m3 - np.ones((2, 4))
print res

print type(haddock)


# Getting started with Matplotlib
# 1

import matplotlib.pyplot as plt

#plt.plot(range(10))
#plt.show()


# 2

times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]

#plt.plot(times, co2)
#plt.show()

#plt.plot(times, co2, 'b--')
#plt.show()

#plt.title("Conc verses time")
#plt.ylabel("Conc")
#plt.xlabel("time")
#plt.show()


# 3

times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#plt.plot(times, co2, times, temp)
#plt.show()
#plt.savefig("tempfigure.pdf")


# Multiple axes and multiple graphs
# 1

import matplotlib.pyplot as plt

#fig, ax1 = plt.subplots()

times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]

#ax1.plot(times, co2)
#ax1.set_ylabel("[CO2]")
#ax2 = ax1.twinx()

temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

#ax2.set_ylabel("Temp (degC)")

#plt.show()


# 2

#plt.subplot(1, 3, 1)

deer = range(0, 10, 1)
#plt.plot(deer)

#plt.subplot(1, 3, 2)

venison = range(10, 0, -1)
#plt.plot(venison)

#plt.subplot(1, 3, 3)

stag = [4] * 10
#plt.plot(stag)

#plt.show()

