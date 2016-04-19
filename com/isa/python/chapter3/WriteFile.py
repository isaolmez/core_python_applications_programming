"Writes to the content user has entered to a file. There is no class or function modularity, just a Python script"

import os

# Store for fast access
newLine = os.linesep

while True:
    fileName = raw_input("Enter a filename: \n")
    if (os.path.exists(fileName)):
        print "Specified file already exists! Please try again."
    else:
        break

lines = [];
while True:
    line = raw_input("Enter a text to write to the file, press x to exit: \n")
    if line == "x":
        break;
    else:
        lines.append(line);

lines = ["%s%s" % (line, newLine) for line in lines]
file = open(fileName, "w");
file.writelines(lines);
file.close();
print "DONE!"
