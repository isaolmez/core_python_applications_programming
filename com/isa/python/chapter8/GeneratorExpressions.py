## Generator Expressions
# Very similar syntax to list comprehensions. But does not create lists and consumes less memory. Values are produced lazily.
file1 = open("test.txt")
print sum(len(word) for line in file1 for word in line.split())

file1.seek(0)
for length in (len(word) for line in file1 for word in line.split()):
    print length,
print


## NOTE: This is a generator. Not a generator expression
def col():
    yield 10
    yield 3
    yield 1
    yield 0


for item in col():
    print item,
print

## From Raw to List to Generator
## First: Read line by line. Less memory usage, but holds onto the file (thus it can block other processes if write operation is done)

def longestLineOld1(fileName):
    longest = 0
    file1 = open(fileName)
    while True:
        length = len(file1.readline().strip())
        if length == 0:
            break
        if length > longest:
            longest = length

    return longest


## Second: Read all at once. More memory usage, but releases file handle more quickly.
# readlines() returns a list with all lines included
def longestLineOld2(fileName):
    longest = 0
    file1 = open(fileName)
    allLines = file1.readlines()
    for line in allLines:
        length = len(line.strip())
        if length == 0:
            break
        if length > longest:
            longest = length

    return longest


## Third. Same as second. There may be less code, but more memory allocation needs to be done, first for readlines() and then list comprehension
def longestLineOld3(fileName):
    longest = 0
    file1 = open(fileName)
    allLines = [line.strip() for line in file1.readlines()]
    for line in allLines:
        length = len(line)
        if length == 0:
            break
        if length > longest:
            longest = length

    return longest


## Fourth: What can we do to prevent excessive memory usage and to shorten the file lock period.
# Firstly, Use file1 object itself as iterator, instead of file1.readlines(). Save on memory usage.
# But in this case, we store all line lengths in a list
def longestLine1(fileName):
    file1 = open(fileName)
    return max([len(line.strip()) for line in file1])

## Fifth: use file1 as iterator and use a generator expression not list comprehension
def longestLine2(fileName):
    file1 = open(fileName)
    return max(len(line.strip()) for line in file1)


print "longest line", longestLineOld1("test3.txt")
print "longest line", longestLineOld2("test3.txt")
print "longest line", longestLineOld3("test3.txt")
print "longest line", longestLine1("test3.txt")
print "longest line", longestLine2("test3.txt")

file1.seek(0)
print type(file1.readlines())
