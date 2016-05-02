## Lambda Expressions: They are just functions, but ANONYMOUS functions
# First let's try to relate regular functions

# 1. Classic way
def echo(arg): return arg


print echo(1)

# Lambda Equivalent: This creates a function, but we must assign it to a reference or call it directly
lambda: "isa"                   # 0 parameter
lambda arg: arg                 # 1 parameter
lambda arg1, arg2: arg1 + arg2  # 2 parameters

# this is a function
print type(lambda x: x)

# 2. Lambda with direct call
print (lambda arg: arg)(1)

# 2. Lambda with reference
echoLambda = lambda arg: arg
print echoLambda(1)
