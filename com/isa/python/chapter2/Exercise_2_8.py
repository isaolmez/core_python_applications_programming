# Basic implementation
tuples = (1, 10, 20, 30, 400)
counter = 0
total = 0
while counter < len(tuples):
    total += tuples[counter]
    counter += 1

print "Sum is:", total

total = 0
for item in tuples:
    total += item

print "Sum is:", total


## Define a function
def calculateTotal(numbers):
    total = 0
    for item in numbers:
        total += item

    print "Sum is:", total


## User input
numbers = list()
for i in range(5):
    number = int(raw_input("Enter a number: "))
    numbers.append(number)

print numbers
calculateTotal(numbers)

parsedTuple = tuple("isa")
print parsedTuple
parsedList = list("isa")
print parsedList
