## Functions can be assignned to other function references
def foo():
    print "in foo"


def bar():
    print "in bar"


foo()
bar()

print "---- Assign function reference to other functions. Make alias"
foo = bar
foo()
bar()


## Function objects can be passed to other functions.
def x(func):
    return func()


def y():
    print "in y"


x(y)


## Example

def convert(func, seq):
    return [func(item) for item in seq]


myseq = (123, 45.67, -6.2e8, 999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
