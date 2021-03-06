# Lists and slicing
# 1

mylist = [1, 2, 3, 4, 5]

print mylist[1]

print mylist[-2]

print mylist[:]

print mylist[1:4]


# 2

one_to_ten = range(1, 11)

print one_to_ten

one_to_ten[0] = 10

print one_to_ten

one_to_ten.append(11)

print one_to_ten

one_to_ten.extend([12, 13, 14])

print one_to_ten


# 3

forward = []
backward = []
print forward
print backward

values = ["a", "b", "c"]

for value in values:
    forward.append(value)
    backward.insert(0, value)

print forward
print backward

forward.reverse()

print forward == backward


# 4

countries = ["uk", "usa", "uk", "uae"]

print dir(countries)

print countries.count("uk")


# Tuples
# 1

t  = (1,)
print t[-1]

sheep = range(100,201)

print sheep

lamb = tuple(sheep)

print lamb[0]
print lamb[-1]


# 2

mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print count, item


# 3

(first, middle, last) = mylist
print first, middle, last

(first, middle, last) = (middle, last, first)
print first, middle, last


# Input and Output
# 1

with open("weather.csv", "r") as reader:
    data = reader.read()
print data


# 2

with open("weather.csv", "r") as reader:
    cattle = reader.readline()
    while cattle:
        print cattle
        cattle = reader.readline()

print "It's over"


# 3

with open("weather.csv", "r") as reader:
    cattle = reader.readline()
    rain = []
    for line in reader.readlines():
        calf = line.strip().split(",")[-1]
        calf = float(calf)
        rain.append(calf)
print rain

with open("myrain.txt", "w") as writer:
    for calf in rain:    
        writer.write(str(calf) + "\n")


# Strings
# 1

s = "I love to write python"
for letter in s:
    print letter

print s[5]

print s[-1]

print len(s)

print s[0], s[0][0], s[0][0][0]


# 2

s = "I love to write python"

split_s = s.split()

print split_s

for cow in split_s:
    if cow.find("i") > -1:
        print "I found 'i' in: '{0}'".format(cow)


# 3

something = "Completely Different"

print dir(something)

print something.count("t")

print something.find("plete")

split_something = something.split("e")

thing2 = something.replace("Different", "Silly")
print thing2

#something[0] = "B"


# Funtions
# 1

def double_it(number):
    return number * 2

print double_it(19)

print double_it(19.5)

print double_it("adil")


# 2

def calc_hypo(a, b):
    hypo = (a**2 + b**2)**0.5
    return hypo

print calc_hypo(3, 4)


# 3

def calc_hypo(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        print "no good - have a conversation with yourself"
        return False
    if a <= 0 or b <= 0:
        print "no good - have a conversation with yourself"
        return False
    else:
        hypo = (a**2 + b**2)**0.5
        print hypo
        return hypo

calc_hypo("adil", 2)

calc_hypo(-2, 4)

calc_hypo(2, 7.89)

