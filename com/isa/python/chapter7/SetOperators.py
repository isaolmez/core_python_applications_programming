## 1. Standard Type Operators
set1 = set([1, 2, 3, 3])  # Removes duplicates
print set1
set2 = set("isa123")
print set2
print 1 in set1
print "i" in set2

print "---- Equality test"
set1Copy = set(set1)
print "set1 == set1Copy", set1 == set1Copy
print "set1 < set1Copy", set1 < set1Copy  # Strictly must be smaller. Equal sets return False with < (smaller than)
print "set1 <= set1Copy", set1 <= set1Copy  # Less Strict. Equal sets return True with <=

set3 = set([1, 2, 3, 4, 5, 6])
print set1 < set3  # All of the == < > could return False. Interesting
print set1 == set3

## Set Type Operators
# union, instersection, difference, symmetric difference: | & - ^
# No + operator
print "---- Set type operators"
set1 = set([1, 2, 3, 4])
set2 = set([4, 5, 6])

print set1 | set2  # union
print set1 & set2  # intersection
print set1 - set2  # difference
print set1 ^ set2  # symmetric difference, XOR
