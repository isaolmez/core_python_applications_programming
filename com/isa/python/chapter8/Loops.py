while True:
    print "loop"
    break;

while 12:
    print "loop"
    break;

s1 = "isa"
for char in s1:
    print char,
print

for index in range(len(s1)):
    print s1[index],
print

for index, char in enumerate(s1):
    print index, char

## range() methods:

for item in range(3):  # range(end) start default to 0. step defaults to 1.
    print item,
print "\n", range(3)

for item in range(10, 0, -1):  # range(start,end, step=1):  It just returns a list and iterates that
    print item,
print "\n", range(10, 0, -1)

## Sequence related functions used in loops
list1 = [5, 1, 2, 4, 3]
for num in list1:
    print num,
print

for num in sorted(list1):
    print num,  ## Does not mutates, returns a new list
print

for num in reversed(sorted(list1)):
    print num,
print
