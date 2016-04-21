def strip(s1):
    s1 = str(s1)
    length = len(s1)
    start = 0
    end = length - 1
    while s1[start].isspace():
        start += 1

    while s1[end].isspace():
        end -= 1

    return s1[start:end + 1]

test ="    isa olmez   \t"
print "-%s-" % test
print "-%s-" % strip(test)
