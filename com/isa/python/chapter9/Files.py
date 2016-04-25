## Built-in file functions

file1 = open("test.txt", "r+")
file2 = file("test2.txt", "w")

## File Only Methods:truncate(), tell(), seek(), read(), readline(), readlines(), write(), writelines(), flush(), close()
file1.truncate()
print file1.tell()
file1.write("hello")
print file1.tell()
print file1.readlines()
file1.seek(0)
print file1.readlines()
print "Offset:", file1.tell()
file1.write(" world!")

# seek() methods
file1.seek(2, 0)
print file1.read()
file1.seek(-10, 1)
print file1.read()
file1.seek(-10, 2)
print file1.read()

# Shows new line in the string representation, not evaluates as a special character
file1.writelines(["\n", "line 2\n", "line 3\n"])
file1.seek(0)
print file1.readlines()
file1.seek(0)
for line in file1:
    print line,
print

## Flush the contents in the buffer
file1.flush()

# Close the file
file1.close()
