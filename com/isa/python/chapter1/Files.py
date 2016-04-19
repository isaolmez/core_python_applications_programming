## Files
## Write a file through w access mode. We have also a for append, + for read/write
## It seems we cannot concetanate strings and integers. We must use str() to produce string values. Like Java's String.valueOf() method.
writeFile = open("test.txt", "w")
for i in range(10):
    writeFile.write("line " + str(i) + "\n")

writeFile.close()

## open() method to open a file and iterates through the lines of the file. This method reads all the file which may be a bottleneck when the file size is big.
# Other alternative way is read one line and output that line. And repeat the process.
readFile = open("test.txt", "r")
for line in readFile:
    print line,

readFile.close()

print

readFile = file("test.txt", "r")
for line in readFile:
    print line,

readFile.close()
