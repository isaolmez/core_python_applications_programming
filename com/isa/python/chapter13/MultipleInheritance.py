# Q: How to access inheritance related information. Like parent class or ancestors.
# A: Through bases atrribute, it seems there is no API
class A(object):
    def __init__(self):
        print "init of A"

    def aMethod(self):
        print "method of A"


class B(object):
    def __init__(self):
        print "init of B"

    def bMethod(self):
        print "method of B"

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print "init of C"


c = C()
print type(C)
print type(c)
print type(type(c))
print C.__bases__


c.aMethod()
c.bMethod()