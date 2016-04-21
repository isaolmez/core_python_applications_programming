import string
import keyword


def CheckKeyword():
    alphas = string.letters + "_"
    numbers = string.digits

    text = raw_input("Enter a valid identifier: \n")
    if keyword.iskeyword(text):
        print "Not a valid identifier. Keyword"
    elif text[0] not in alphas:
        print "Not a valid identifier"
    else:
        alphanums = alphas + numbers
        for char in text[1:]:
            if char not in alphanums:
                print "Not a valid identifier"
                break  ## What is break doing??
        else:
            print "OK. A valid identifier"


def CheckKeywordCustom():
    alphas = string.letters + "_"
    numbers = string.digits
    keywords = keyword.kwlist
    text = raw_input("Enter a valid identifier: \n")
    if text in keywords:
        print "Not a valid identifier. Keyword"
    elif text[0] not in alphas:
        print "Not a valid identifier"
    else:
        alphanums = alphas + numbers
        for char in text[1:]:
            if char not in alphanums:
                print "Not a valid identifier"
                break  ## What is break doing??
        else:
            print "OK. A valid identifier"

CheckKeywordCustom()