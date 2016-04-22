## Auxiliary Statements: break, continue, pass

while True:
    break

num = -1
while num < 10:
    num += 1
    print num,
    if num % 2 == 0:
        continue

print

while False:
    pass


def test(): pass


list1 = [1, 2, 3, 4, 5]
for item in list1:
    if item == 10:
        break
else:
    print "There is no 10 in the list"
