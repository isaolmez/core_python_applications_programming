input = raw_input("Enter a string: \n")
counter = 0
while counter < len(input):
    print input[counter],
    counter += 1

print

for i in range(len(input)):
    print input[i],

print

for c in input:
    print c,

print

for i, c in enumerate(input):
    print c,
