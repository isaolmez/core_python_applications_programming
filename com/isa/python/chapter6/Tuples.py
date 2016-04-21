## Tuples are very similar to lists; but they are immutable
tuple1 = (1,2,3)
print tuple1
# For tuples, parantheses are redundant and this expression craetes a tuple.
# For lists we must use brackets
tuple2 = "a", "b", "c"
print tuple2

# tuple1[1] = 99 # ERROR: We cannot mutate tuple or assign new values to its elements
print tuple
tuple1 = (0, 0, 0) #  But we can assign a completely new tuple
print tuple1

# Cannot delete individual elements; but can delete tuple itself
# del tuple1[1] # ERROR: We cannot mutate
del tuple1
