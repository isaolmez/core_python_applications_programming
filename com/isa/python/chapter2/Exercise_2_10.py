while True:
    try:
        input = raw_input("Enter a number between 1 and 100: \n")
        number = int(input)
        if number >= 1 and number <= 100:
            print "Thanks, exiting now..."
            break
        else:
            print "Please enter a number in the range!"

    except Exception, e:
        print "Please enter a valid number!"
