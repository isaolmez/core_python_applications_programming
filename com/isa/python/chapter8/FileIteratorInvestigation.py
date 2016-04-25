import time


## Investigate if file iterator holds the handle or not
## First: Holds the file handle till the end

def handleCheck(fileName):
    file1 = open(fileName)
    while True:
        line = file1.readline().strip()
        if line == '':
            break
        print line
        time.sleep(5)


## Second: Does not hold handle for too long and releases after reading. But memory intensive.
def handleCheck2(fileName):
    file1 = open(fileName)
    allLines = file1.readlines()
    for line in allLines:
        print line


## Third: What happens when iterator returns but processing is continuing?
# Iterator does not release the lock. So it has the same effect with first example
# def dummy(text):
#     time.sleep(10)
#     return text


def handleCheck3(fileName):
    file1 = open(fileName)
    for line in file1:
        print line.strip()
        time.sleep(5)


## Fourth: This uses file iterator like third example bu uses less memory. Because it does not store the lengths as list.
# And in fact it has characteristics with the first example, but with less code.

def handleCheck4(fileName):
    file1 = open(fileName)
    for line in (line.strip() for line in file1):
        print line
        time.sleep(5)




## Fifth: The only difference between first and this is reading of line is in a different function. It does not release the handle
def readFile(fileName):
    file1 = open(fileName)
    while True:
        line = file1.readline().strip()
        # print "Inner", line
        if line == "":
            break
        yield line


def handleCheck5(fileName):
    for line in readFile(fileName):
        print line
        time.sleep(5)

# handleCheck("test3.txt")

# handleCheck2("test3.txt")

# handleCheck3("test3.txt")

# handleCheck4("test3.txt")

handleCheck5("test3.txt")
