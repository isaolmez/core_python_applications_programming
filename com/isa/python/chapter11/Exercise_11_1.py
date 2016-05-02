def countToFour1():
    for eachNum in range(5):
        print eachNum,


def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum,


def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum,


print "countToFour2"
print
# countToFour1(2)
# countToFour1(4)
# countToFour1(5)
countToFour1()
print

print "countToFour2"
countToFour2(2)
print
countToFour2(4)
print
countToFour2(5)
print
# countToFour2()

print "countToFour3"
countToFour3(2)
print
countToFour3(4)
print
countToFour3(5)
print
countToFour3()
print
