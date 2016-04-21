def forwardAndReverse(s1):
    length = len(s1)
    for item in range(length):
        print s1[item], " - ", s1[length - 1 - item]


def match(s1, s2):
    s1 = str(s1)
    s2 = str(s2)
    if s1 == None or s2 == None:
        return False
    elif len(s1) != len(s2):
        return False
    else:
        length = len(s1)
        for item in range(length):
            sub1 = s1[item]
            sub2 = s2[item]
            if sub1 != sub2:
                return False
            elif sub1.isupper() and sub2.islower() or sub1.islower() and sub2.isupper():
                return False
            else:
                pass
    return True


def isPalindromic(s1):
    length = len(s1)
    for item in range(length / 2 + 1):
        if s1[item] != s1[
                            length - 1 - item]:  ## Allows slice/index operator although it does not whether it is a sequence type or not. Possible runtime error.
            return False
    return True


def makePalindromic(s1):
    reverseString = "".join([char for char in reversed(s1)])
    return "".join([s1, reverseString])


s1 = "helloworld!"
s2 = "helloworlD!"
forwardAndReverse(s1)
print match(s1, s2)
pal = "abcdedcba"
print isPalindromic(pal)
print isPalindromic("abcdca")
print makePalindromic("asi")
