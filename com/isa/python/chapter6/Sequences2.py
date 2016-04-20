text = "isaolmez"

## Slices
for item in text:
    print item,

print

for item in text[0::1]:
    print item,

print

for item in text[-1::-1]:
    print item,

print

print text[0:5:2]
print text[::-1]
print text[-1::-1]
print text[0::-1]
print text[:None] # None is equivalent to no literal at all

print "\n---Multiple prints"
for item in range(len(text), 0, -1):
    print text[:item]

print

for item in [None] + range(-1, - len(text), -1): # concatenate the list
    print text[:item]

print

first = [1,2,3,4]
second = list(first)
print id(first) == id(second)