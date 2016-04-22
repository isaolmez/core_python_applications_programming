## Sets:not special syntax for creation. use set() and frozenset() functions

# Create
set1 = set("dragon")
set2 = frozenset("dragon")
print set1, "length:", len(set1), "type:", type(set1)
print set2, "length:", len(set2), "type:", type(set2)
set3 = set(["a", "b", "c", "d"])
print set3

# Access: iterate only or probe by membership check using in
print "d" in set1
for item in set1:
    print item,
print

# Update: Only mutable sets can be updated(elements are added/modified/deleted). frozenset does not allow these operations.
set1.add("isa")  # Mutated. Adds ONE element
print set1
set1.update(set3)
print set1
set1.update("123")  # Adds 3 substring as elements.
print set1

# Remove
set1.remove("1")
print set1
set1 = set1 - set(
    "123")  # It supports minus operator. But does NOT support plus(concatenation) operator because of uniqueness constraint
print set1
# set1 = set1 + set("123")

# Delete: Cannot delete individual member because we do not have a way to reach them.
# We can delete the set object
del set1
