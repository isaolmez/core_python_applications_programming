text = "a"
text2 = str()
obj = object()
print id(text), id(text2), id(obj)

if not None:
    print "It is false"

if not 0:
    print "It is zero integer"

if not 0.0:
    print "It is zero float"

if not "":
    print "It is empty string"

if not []:
    print "It is empty list"

if not ():
    print "It is empty tuples"

if not {}:
    print "It is empty dictionary"

mylist = [0, 1, 2, 3, 4, 5, 6, 7]
for item in mylist[::-1]:
    print item,

print

for item in mylist[0::2]:
    print item,

print

multi = [[1, 2, 3, 4], [5, 6, 7, 8]]
for item in multi[0:3]:
    print item,

print
