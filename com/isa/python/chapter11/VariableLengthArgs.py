## Non-Keyword Varargs - Tuple
# Must come after formal arguments/parameters both in definition and invocation

def foo(arg1, arg2=2, *arg3):
    print arg1, arg2, arg3


foo(1)
foo(1, 2)
foo(1, 2, 3, 4, 5, 6)


# foo(arg2=22, arg1=11, 0,0,0,0) # Runtime Error: we cannot use keyword arguments with grouped arguments.


# Keyword Varargs: Must come after non-keyword vararg arguments/parameters both in definition and invocation
def foo(a, b=1, *t, **d):
    print "formal a:", a
    print "formal b:", b
    for item in t:
        print "informal non-keyword:", item

    for item in d:
        print "informal keyword:", item, d[item]


foo(1)
foo(1, 2, 3, 4, 5, d1=0, d2=0)
foo(1, 2, *(3, 4, 5), **{"d1": 0, "d2": 0})

tuple1 = (3, 4, 5)
dict1 = {"d1": 0, "d2": 0}
foo(1, 2, *tuple1, **dict1);


## we can only use tuple and dictionary syntax, namely informal parameters/arguments instead of formal parameters/arguments
