## Decorators in Pyhton
# * take a function as argument
# * adds code before or after the actual function.
# * define an inner function
# * and finally returns that inner function.
from time import ctime, sleep


## Inner function declaration
def decFoo(func):
    def wrappedFunc():
        print "[%s] %s() is called" % (ctime(), func.__name__)
        result = func()
        print "[%s] %s() is finished" % (ctime(), func.__name__)
        return result

    return wrappedFunc


## Decorator: Original function is passed to the decorator function. Decorator function inserts some logic and returns another function containing the original.
# 1st way
@decFoo
def foo():
    return 1


print "Result: %d" % foo()


# How can we achive same result without decorators ?
# 2nd way
def foo():
    sleep(1)
    return 1


print "Result: %d" % decFoo(foo)()
