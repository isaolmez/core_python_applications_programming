## 2-6
num = 12
if num < 0:
    print "Negative"
elif num == 0:
    print "Zero"
else:
    print "Positive"

while True:
    input = raw_input("Enter a number: \n")
    if (input == "x"):
        break

    num = int(input)
    if num < 0:
        print "Negative"
    elif num == 0:
        print "Zero"
    else:
        print "Positive"
