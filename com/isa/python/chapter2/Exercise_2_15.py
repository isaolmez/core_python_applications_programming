## a. Sort

numbers = list()
for i in range(3):
    number = int(raw_input("Enter a number:"))
    numbers.append(number)

a = numbers[0]
b = numbers[1]
c = numbers[2]

if b < a:
    temp = a
    a = b
    b = temp

if c < a:
    temp = a
    a = c
    c = temp

if c < b:
    temp = b
    b = c
    c = temp


print "Ascending Order:", a, b, c
print "Descending Order", c, b, a