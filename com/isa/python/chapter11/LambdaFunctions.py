## Lambda Expressions: They are just functions
# First let's try to relate regular functions

def echo(arg): return arg


print echo(1)

# Lambda Equivalent: This creates a function, but we must assign it to a reference or call it directly
lambda arg: arg

print (lambda arg: arg)(1)

