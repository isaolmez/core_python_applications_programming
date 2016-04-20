import string
alphas = string.letters + "_"
numbers = string.digits

text = raw_input("Enter a valid identifier: \n")

if text[0] not in alphas:
    print "Not a valid identifier"
else:
    alphanums = alphas + numbers
    for char in text[1:]:
        if char not in alphanums:
            print "Not a valid identifier"
            break                           ## What is break doing??
    print "Loop done."
    print "OK. A valid identifier"

