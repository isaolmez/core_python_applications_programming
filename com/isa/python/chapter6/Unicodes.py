# -*- coding: utf-8 -*-

u1 = unicode("a")
print u"\xc2"
print type(u1)
print type(str(u1))

CODEC = "utf-8"


def writeToFile(fileName):
    text = "Hello World!"
    try:
        targetFile = open(fileName, "w")
    except IOError, e:
        print e
    else:
        targetFile.write(text)
        targetFile.close()


def readFromFile(fileName):
    try:
        targetFile = open(fileName, "r")
    except IOError, e:
        print e
    else:
        print targetFile.readlines()  # Bulk read all lines
        targetFile.close()


def writeUnicodeToFile(fileName):
    text = u"Hello World!§§"  # If you do not put u prefix, it is by default ASCII string.
    try:
        targetFile = open(fileName, "w")
    except IOError, e:
        print e
    else:
        encoded = text.encode(CODEC)  # Encoded bytes
        targetFile.write(encoded)
        targetFile.close()


def readUnicodeFromFile(fileName):
    try:
        targetFile = open(fileName, "r")
    except IOError, e:
        print e
    else:
        # bytes_in = targetFile.read()
        bytes_in = targetFile.readlines()
        print bytes_in, type(bytes_in)
        for item in bytes_in:
            print item.decode(CODEC)  ## try with utf-16

        print [line.decode(CODEC) for line in bytes_in]
        targetFile.close()


writeToFile("ascii.txt")
readFromFile("ascii.txt")
writeUnicodeToFile("unicode.txt")
readUnicodeFromFile("unicode.txt")
