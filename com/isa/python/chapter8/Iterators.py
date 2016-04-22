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
