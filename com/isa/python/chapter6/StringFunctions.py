## 1. Standard Type Functions: can be applied to most classes
# cmp()
print "---- Standard type functions"
s1 = "a"
s2 = "b"

print cmp(s1, s2)
print cmp(s2, s1)
print cmp(s1, "a")
print cmp("a", "a")

## 2. Sequence Type Functions: can be applied to all sequence types including strings
# len(), max(), min(), enumerate(), zip(), sorted(), reversed()
print "---- Sequence Type Functions"
print len("abc")
print max("abc")
print min("abc")
print sorted("isa")
for item in reversed("isa"):
    print item,
print
for i, c in enumerate("abc"):
    print "index:", i, "character:", c

s1, s2 = "abc", "123"
print zip(s1, s2)

## 3. String Type functions: raw_input(), str(), unciode(), chr(), ord() and unichr()
print "---- Factory functions"
s1 = str("a")
u1 = unicode("u")
print type(s1) is str
print type(s1) is unicode
print type(
    s1) is basestring  ## There is differnce between type() and isinstance() method. Seems like isinstance() also considers parent classes in inheritance tree.
print isinstance(s1, str)
print isinstance(s1, unicode)
print isinstance(s1, basestring)

# chr(), ord() and unichr()
print chr(65)
print ord(chr(65))

print ord("a")
print chr(ord("a"))
