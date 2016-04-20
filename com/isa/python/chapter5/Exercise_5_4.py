def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


print "1992:", isLeapYear(1992)
print "1996:", isLeapYear(1996)
print "2000:", isLeapYear(2000)
print "1967:", isLeapYear(1967)
print "1900:", isLeapYear(1900)
print "2400:", isLeapYear(2400)
