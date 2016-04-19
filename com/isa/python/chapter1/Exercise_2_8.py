tuples = (1, 20, 400)
counter = 0
sum = 0
while counter < len(tuples):
    sum += tuples[counter]
    counter += 1

print "Sum is:", sum

sum = 0
for item in tuples:
    sum += item

print "Sum is:", sum
