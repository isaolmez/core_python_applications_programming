numbers = [1, 3, 5, 7, 11]
sum = 0
for number in numbers:
    sum += number

print "Total is:", sum
print "Average is:", sum / 5
print "Real average is:", float(sum) / 5  ## It does not need both operands to be floating point numbers

## Function
def calculateAverage(numbers):
    sum = 0
    for number in numbers:
        sum += number

    print "Real average is:", float(sum) / len(numbers)

def readNumbers(counter):
    numbers = list()
    for i in range(counter):
        number = int(raw_input("Enter a number:"))
        numbers.append(number)
    return numbers

calculateAverage(readNumbers(5))

num = long(5)
print type(num)
num = 5
print type(num)
num = 5L
print type(num)
num = 1.3
print type(num)
