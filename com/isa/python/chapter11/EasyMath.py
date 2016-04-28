from random import randint, choice
from operator import add, sub

ops = {"+": add, "-": sub}
MaxTries = 3


def askQuestion():
    # Generate two numbers
    # operand1 = randint(0, 10)
    # operand2 = randint(0, 10)
    operator = choice(ops.keys())
    operatorFunction = ops.get(operator)
    # actualResult = operatorFunction(operand1, operand2)
    operands = [randint(0, 10) for num in range(2)]
    actualResult = operatorFunction(*operands)
    tries = 0
    print "What is the result of %s %s %s" % (operands[0], operator, operands[1])
    while True:
        response = int(raw_input())

        if response == actualResult:
            print "Correct!"
            break
        elif response != actualResult:
            tries += 1
            print "Not correct! Number of tries:", tries

        if tries == MaxTries:
            print "You have reached max tries! Result is:", actualResult
            break
        else:
            print "Try again!"


def main():
    while True:
        askQuestion()
        newQuestion = raw_input("Do you want to contine? \n0 - No \n1 - Yes")
        if newQuestion == "1":
            continue
        else:
            break;

    print "See you later!"


if __name__ == "__main__":
    main()
