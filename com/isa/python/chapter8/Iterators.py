## Two things can be iterated:
# 1. Sequences through number indexing generally starting from 0
# 2. Iterators through some interface exposing next() method. iter() is to craete a new iterator.

# 2. Iterators.
# i. Sequences can be made iterators
# ii. Other types can be made iterators

# i. Sequences
list1 = [1, 2, 3, 4, 5, 6]
iter1 = iter(list1)
print iter1.next(), iter1.next(), iter1.next(), iter1.next(), iter1.next(), iter1.next()

# If there is no next element, an exception is thrown
try:
    print iter1.next()
except StopIteration, s:
    print "Iterator has beem exhausted", s
else:
    print "Whew, without exception"

# For loop automatically converts sequences to iterators and handles exceptions
for item in list1:
    print item,
print

# is equivalent to
iter1 = iter(list1)
try:
    for item in iter1:
        print item,
except StopIteration, s:
    pass

# or

print
iter1 = iter(list1)
while True:
    try:
        print iter1.next(),
    except StopIteration, s:
        break

## Dictionaries as iterables
print "---- Dictionaries"
d1 = {1: 1, 2: 2}
print type(d1.keys()), d1.keys()
print type(d1.values())
print type(d1.items())
print type(
    d1.iterkeys()), d1.iterkeys()  # iterator string representation is not its contents, but the info about the object
print type(d1.itervalues())
print type(d1.iteritems())

## Files
print "---- Files"
file1 = open("test.txt", "r")
for line in file1:
    print line,
print

## Mutation during iteration
list1 = [0, 1, 2, 3]
for item in list1:  # Iterator logic seems to depend on the rank of item.
    print item
    if item == 0:
        del list1[0]

## iter(obj), iter(func, sentinel)
list1 = [1, 2, 3, 4]

# Let's try sentinel
import random


def iterFunc():
    return random.choice([0, 1, 2, 3, 4])


for item in iter(iterFunc, 0):
    print item,
print
