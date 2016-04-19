## Everything in Python is an object. There is no primitive types such as int, long like Java. And variables (reference variables in Java) refer to the object.
## This allows multiple variables refer to the same object

# But immutability provides the sense of processing primitives. Like Java Strings.
x = 3.14
y = x
print x, y

## del deallocates the variable
del x
# print x # Gives error


## Dynamic typing
x = 3
print type(x)
x = "isa"
print type(x)
