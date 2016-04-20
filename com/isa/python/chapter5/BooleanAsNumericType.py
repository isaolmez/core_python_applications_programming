## Boolean is in fact a numeric type

print bool(1)
print bool(0)
print bool("1")
print bool("0")
print bool("")
print bool([])

print "Boolean arithmetic"
print True + True
print True + False
print "True == 1:", True == 1
print "True + True + 100:", True + True + 100

class Test(object):
    pass

print "bool(Test())", bool(Test())

class Test2(object):
    def __nonzero__(self):
        return False

print "bool(Test2())", bool(Test2())