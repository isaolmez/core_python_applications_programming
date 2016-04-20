## Sequences
# 1. Strings
# 2. Lists
# 3. Tuples

## Membership
# We have found contains() method
text = "isaolmez"
print "i" in text
print "y" in text

firstList = [1, 2, 3, 4, 5]
firstTuple = (1, 2, 3, 4, 5)
print 1 in firstList
print 1 in firstTuple
print 22 in firstList
print 22 in firstTuple

## Concatenation
secondList = [6, 7]
secondTuple = (6, 7)
result = firstList + secondList
print result
print firstTuple + secondTuple
# Alternate version for lists : extend()
print "Before extend:", id(firstList)
firstList.extend(secondList)
print firstList
print "After extend:", id(firstList)  # We have mutated the list.

## Repetition
print text * 2;
print firstList * 2
print firstTuple * 2
