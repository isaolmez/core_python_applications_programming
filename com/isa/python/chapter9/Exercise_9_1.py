import time

## With custom iterator
file1 = open("9_1.txt")


def readLine():
    return file1.readline()


def filterComments():
    fileIterator = iter(readLine, "")
    for line in fileIterator:
        line = str(line)
        if not line.startswith("#"):
            print line,


filterComments()


## With default file iterator
def filterComments2(fileName):
    f1 = open(fileName)
    for line in f1:
        if not line.startswith("#"):
            print line,


filterComments2("9_1.txt")

## With generator
file1.seek(0)


def lineGenerator():
    while True:
        line = file1.readline()
        if line == "":
            break
        else:
            yield line


def filterCommentsWithGenerator():
    for line in lineGenerator():
        if not line.startswith("#"):
            print line,


filterCommentsWithGenerator()
