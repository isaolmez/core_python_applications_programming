## Comparison related builtin functions
if cmp(1, 2) == 0:
    print "1 and 2 are equal"
elif cmp(1, 2) < 0:
    print "1 is smaller than 2"
else:
    print "1 is greater than 2"

if cmp("a", "a") == 0:
    print "a == a"

## repr() str() `` functions
# repr() and `` are identical. These are string representations for the interpreter
# str() gives string representation of an object in a human readable format
print repr([1, 2, 3, 4])
print `[1, 2, 3, 4]`
print str([1, 2, 3, 4])
print type([1, 2, 3, 4])
print type(type([1, 2, 3, 4]))

print type(4)
print type(object)

## eval() and repr() can be used to recreate an object. str() can also be used, if it outputs the string representation valid for eval.
recreated = eval("[1,2,3,4]")
print "Type of recreated is", type(recreated)


class Test(object): pass


class BareClass: pass


print type(Test)
print type(Test())
## It does not print the name of BareClass. It prints instance and type
print type(BareClass)
print type(BareClass())

## call type() function on imported modules and classes
import Comparison
print type(Comparison.MyClass)
print type(Comparison.MyClass())
