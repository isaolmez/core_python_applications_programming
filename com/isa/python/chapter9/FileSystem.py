## os module
# import statement also loads os.path module.
import os

print [os.sep]
print [os.linesep]

# File Processing Functions
file1 = open("test.txt", "w+")
print os.stat("test.txt"), type(os.stat("test.txt"))

open("temp.txt", "w").write("hello")
os.rename("temp.txt", "temp2.txt")
os.remove("temp2.txt")

# Walks the directory tree from given root
for item in os.walk("/home/isa/Downloads"):
    print item

# Lists files
for item in os.listdir("/home/isa/Downloads"):
    print item,

print os.access("/root", 1)

## os.path module
# Seperation functions
print "---- Seperation"
absPath = os.path.abspath("test.txt")
print absPath
print os.path.basename(absPath)
print os.path.dirname(absPath)
print os.path.split(absPath)
print os.path.splitext(absPath)

# Information functions
print "---- Information"
print os.path.getatime(absPath), os.path.getctime(absPath), os.path.getmtime(absPath), os.path.getsize(absPath)

# Inquiry
print "---- Inquiry"
print os.path.exists("test.txt")
print os.path.exists("test11.txt")
print os.path.isdir(absPath)
print os.path.isdir(os.path.dirname(absPath))
print os.path.isabs(absPath)
