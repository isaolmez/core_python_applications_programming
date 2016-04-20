## There are two types again
# 1. Conversion functions or constructor functions or factory functions
# 2. Operational functions

## Conversion
firstList = [1, 2, 3]
firstTuple = (1, 2, 3)
firstStr = "isa"
print unicode(firstStr);
print list(firstTuple)
print list(firstStr)
print tuple(firstList)
print tuple(firstStr)
print str(firstList)
print str(firstTuple)
print str(firstStr)

## It seems that for immutable sequences like string and tuple, factory methods return exactly the same object.
# For mutable type list, it returns a new list object
print "Identity check after factory methods"
print id(firstStr) == id(str(firstStr))
print id(firstTuple) == id(tuple(firstTuple))
print id(firstList) == id(list(firstList))

## Check previous behaviour with the sequences that have same values but different type
print id(firstList) == list(firstTuple)
print id(firstTuple) == tuple(firstList)

## Shallow copy test
target = list(firstTuple)
target[0] = 99 # This does not affect other anyway, because this alias is being reassigned. However, even if I try to change state of object, it will return a new object if it is immutable. It must be mutable.
print target
print firstTuple

## Operational Functions

