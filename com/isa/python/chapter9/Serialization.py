## Serialization and deserialization using pickle
# Other alternatives are: marshall, shelve vs..

import pickle

list1 = [1, 2, 3, "a", "b", "c"]
file1 = open("dump.txt", "w+")
pickle.dump(list1, file1)
file1.seek(0)
print file1.readlines()

file1.seek(0)
print pickle.load(file1)
