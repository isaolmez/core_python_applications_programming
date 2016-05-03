# Differences with Java:
# There are no access modifiers such as public, private protected
# There are no abstract methods
# Instance methods are in fact class attributes and can be called through both instances and classes
# Since there is no declaration/initialization like in Java, instance variables must be defined within instance methods using self.


class Test(object):
    classVar1 = 11
    def test(self):
        x =10
        self.instanceVar1 = 99
        return x


## Instance Creation
i = Test()
print type(i)
print type(type(i))
print type(type(type(i)))

print type(i) is Test
print isinstance(i, (Test))
print isinstance(i, (type)) ## does not behave like Java's instanceof operator. Only compares direct parent


print i.test()
print i.classVar1
print Test.classVar1
print i.instanceVar1
# print Test.instanceVar1   # ERROR cannot access through class

# Temporary variables
i.temp1 = "temp"    # Instance is used as a namespace
print i.temp1

