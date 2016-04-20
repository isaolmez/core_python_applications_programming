## 1. Sequence Functions: Can be applicable to all sequence types including strings

s1 = "a"
s2 = "b"

print cmp(s1, s2)
print cmp(s2, s1)
print cmp(s1, "a")
print cmp("a", "a")

print len("abc")
print "abc"

print max("abc")
print min("abc")

for i,c in enumerate("abc"):
    print "index:",i,"character:",c

s1, s2 = "abc", "123"
print zip(s1,s2)

## Factory functions: str() unciode()
print "---- Factory functions"
s1 = str("a")
u1 = unicode("u")
print type(s1) is str
print type(s1) is unicode
print type(s1) is basestring ## There is differnce between type() and isinstance() method. Seems like isinstance() also considers parent classes in inheritance tree.
print isinstance(s1, str)
print isinstance(s1, unicode)
print isinstance(s1, basestring)

# chr(), ord() and unichr()
print chr(65)
print ord(chr(65))

print ord("a")
print chr(ord("a"))