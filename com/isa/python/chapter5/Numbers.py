## Numbers are immutable OBJECTS. They are scalar, immutable and direct.
# Scalar: They only contain one value
# Immutable:  You cannot change the value of number object (int, long, boolean, float, complex number)
# Direct: You access directly by specifying the variable. Not through indexing(sequential access) and not through keys (hasked key - value mapping)

# id() returns different values after each assignment, because a new object is created after each assignment.
number = 12
print id(number)
number = 14
print id(number)