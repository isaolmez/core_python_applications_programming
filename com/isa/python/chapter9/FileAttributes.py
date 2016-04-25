## File attributes
file1 = open("test.txt", "w+", )
file1.write("isa".encode("utf-8"))
file1.flush()
file1.seek(0)
print file1.readlines()
print "Name", file1.name
print "Encoding", file1.encoding
print "Mode", file1.mode
print "New lines", file1.newlines
print "Is closed?", file1.closed
