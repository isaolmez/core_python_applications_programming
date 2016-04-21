## 1. Standard Type Operators: can be applied to most types
# cannot apply concatenation and repetition, because of the uniqueness constraint

d1 = {1: 1, 2: 2, 3: 3}
d2 = {1: 2, 2: 3, 3: 4}
print d1 == d2
print d1 < d2
print d1 > d2

## 2. Mapping Type Operators: can be applied to mapping types
# There is one mapping type, so there is no third branch like sequences.
d1 = {"a": "aa", "b": "bb"}
print d1["a"]

print "a" in d1
print 12 in d1
