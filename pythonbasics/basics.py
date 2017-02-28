print 'hello'

b = 5
c = 10

a = b ** 2 + c ** 2
a = a ** 0.5

print a

a = int(a)

print type(a)

#egg = 5
#while eggs <  6:
#    print 'buy more eggs'

mylist = [23, 'hi', 2.4e-10]
count = 0
while count < 3:
    item = mylist[count]
    print item, mylist.index(item)
    count += 1

x = 1
if x: print x, " is True"

if 22.1: print "True"

if "hello": print "True"

if [1, 2]: print "True"

if 0: print "True"

if 0.0: print "True"

if False: print "True"

if None: print "True"

if "": print "True"

if []: print "True"

if {}: print "True"

if (): print "True"
