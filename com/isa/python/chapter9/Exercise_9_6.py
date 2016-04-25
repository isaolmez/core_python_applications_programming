import os

f1 = open("test.txt")


def isSame(fileName1, fileName2):
    # 1: check sizes
    if os.stat(fileName1).st_size != os.stat(fileName2).st_size:
        return False

    # 2:Compare bytes
    f1 = open(fileName1)
    f2 = open(fileName2)
    while True:
        byte1 = f1.read(1)
        byte2 = f2.read(1)
        if byte1 != byte2:
            return False

        if byte1 == "":
            return True


print isSame("a1.txt", "a2.txt")
