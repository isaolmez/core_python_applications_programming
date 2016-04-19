## Can create lists with a single line. Like Java's anonymous array creation, but like on steroids.
myList = [i for i in range(5)]
for item in myList:
    print item,
print

# Odd numbers
oddNumbers = [i for i in range(100) if i%2 == 1]
for item in oddNumbers:
    print item,
print

# Squares of odd number
oddNumbers = [i ** 2 for i in range(100) if i%2 == 1]
for item in oddNumbers:
    print item,
print