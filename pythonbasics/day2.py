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


#3

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


#4

countries = ["uk", "usa", "uk", "uae"]

print dir(countries)

print countries.count("uk")
