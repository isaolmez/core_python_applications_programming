def readNumbers(counter):
    numbers = list()
    for i in range(counter):
        number = int(raw_input("Enter a number:"))
        numbers.append(number)
    return numbers

## Function
def calculateAverage(numbers):
    sum = 0
    for number in numbers:
        sum += number

    print "Real average is:", float(sum) / len(numbers)

## Define a function
def calculateTotal(numbers):
    total = 0
    for item in numbers:
        total += item

    print "Sum is:", total


while True:
    input = raw_input("""Choose your operation:
    Press 1 for sum of numbers:
    Press 2 for avarage of numbers:
    Press x to exit:
    """)
    if input == "x":
        break
    elif input == "1":
        calculateTotal(readNumbers(5))
    elif input == "2":
        calculateAverage(readNumbers(5))
    else:
        print "Choose a valid option"