# Partial Function Application: Fixing some parameters
# Change base to 2 for int conversion
from functools import partial  # Must be imported from functools


# Formal arguments
def func(a, b):
    return a, b


funca = partial(func, "isa")
print funca("olmez")

# Cascading partial
funcab = partial(funca, "olmez")
print funcab()

## Lets try with informal arguments

print max(99, 155)
maxWith99 = partial(max, 99)
print maxWith99(155)

# keyword argument usage is needed if given argument is later in position. And not the first
print int("11111", 2)

int2 = partial(int, base=2)

print int2("11111")

# Cascading: make another partial function from existing partial function by providing additional fixed arguments.
maxWith99And155 = partial(maxWith99, 155)
print maxWith99And155(200)
