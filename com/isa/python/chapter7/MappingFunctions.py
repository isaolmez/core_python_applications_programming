## 1. Standard Type Functions:
# type(), str(), cmp()

d1 = {"a": "1"}
print type(d1)
# cmp() Compare strategy: First length, then key compare by iterating, then value compare by iterating
d2 = {"a": "1", "b": "2"}
print cmp(d1, d2)
d1["b"] = "3"
print cmp(d1, d2)
d1["b"] = "2"
print cmp(d1, d2)
d1["c"] = "3"
print cmp(d1, d2)
d2["c"] = "4"
print cmp(d1, d2)
d2["c"] = "3"
print cmp(d1, d2)

print zip([1, 2], [3, 4])
print zip((1, 2), (3, 4))

## 2. Mapping Type Functions
# Shallow copies
d1 = dict()
d2 = dict(x=1, y=2, z=3, list=[1, 2])
print d1, d2
d3 = d2.copy()
print d3
d3["list"][0] = 99
print d2["list"], d3["list"]    # Shallow copy

# Deep Copies
import copy
d4 = copy.deepcopy(d2)
d4["list"][0] = 11
print d2["list"], d4["list"]    # Deep copy


# len(), hash()
print len(d3)

print hash(12), hash(12.0), hash(12.33), hash("isa") # Equal float and int values hash to the same number
