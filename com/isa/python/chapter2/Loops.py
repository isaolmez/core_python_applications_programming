counter = 0;
while counter < 10:
    print counter
    counter += 1

## Usage of parantheses can make code more like Java. Also note the usage of print keyword. It is not a function, but it feels like it when we use parantheses.

counter = 0;
while (counter < 10):
    print(counter);
    counter += 1;

## Pythons for loop is like foreach of Java. It iterates through an Iterable. We dont have a classic for loop that is used with a counter. Also it uses in keyword as C#.
## print statements by default adds a new line character. To prevent this, put comma to the end, This also puts a space between elements. Much like Java's println and print statements.
list = ["isa", "ali", "veli"]
for item in list:
    print item,

print
for item in [1, 2, 3, 4, 5, 6]:
    print item,

print
for item in ("isa", "ali", "veli"):
    print item,

print
for item in (1, 2, 3, 4, 5, 6):
    print item,

print
for item in {"a": 1, "b": 2, "c": 3}:
    print item,

print

## Print statement with placeholders
who = "isa"
what = "hey"

print "I am", who, "and I say", what, what, what, what
print "I am %s and I say %s" % (who, (what + " ") * 4)

## For loops that mimic class counter-based for loops. we use a list composed of consecutive integers.
# We can also use range() function
for item in [0,1,2]:
    print item,
print

# length is exclusive. Meaning that it contains 0,1,2
for item in range(3):
    print item,
print

## Iterate over string charachters
for char in "isa":
    print char,
print

foo = "isa"
for i in range(len(foo)):
    print "we have", foo[i], "in character position:",i

for i,c in enumerate(foo):
    print "we have",c,"in character position:",i



