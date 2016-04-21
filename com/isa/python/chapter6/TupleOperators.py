## Tuple operators are very similar to lists
# Slice operator for tuples is used for only read-access. Like strings. Remember that lists are mutable and slice operator can be used for read and write access

# It is the default collection type if no parantheses, brackets, vs. used.
tuple1 = 1, 2, 3, 4
tuple2 = 0, 0, 0, 0

# But it is recommended to use identifying symbols to avoid side effects like below.
print tuple1 < tuple2
print 1, 2, 3, 4 < 0, 0, 0, 0


##It probably does not help your case that the parentheses are also overloaded as the expression grouping
# operator. Parentheses around a single element take on that binding role rather than serving as a
# delimiter for tuples. The workaround is to place a trailing comma (,) after the first element to indicate
# that this is a tuple and not a grouping.

single = ("abc")
print type(single)  # NOT a tuple but a string
single = ("abc",)
print type(single)  # Force it by using a trailing comma
single = tuple("abc")
print type(single)  # Or use tuple() factory function to explicitly specify the type