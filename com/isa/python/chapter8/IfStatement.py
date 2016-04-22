## If statements
if 1:
    print "Evaluated to true"

if True:
    print "True"

if 1 < 2 and 2 < 3 and 1 < 2 < 3:
    print "True"

if 1 < 2: print "True"

if True:
    pass
elif True:
    pass

choice = "update"
if choice == "add":
    print "add item"
elif choice == "update":
    print "update item"
elif choice == "delete":
    print "delete item"
else:
    print "invalid choice"

## Switch like statement can be simulated with dictionary
choices = {"add": "add item", "update": "update item", "delete": "delete item"}
print choices.get(choice, "invalid choice")

x = 4
y = 3
print (x < y and [x] or [y])[0]  # This is some nasty syntax relying on bit operations. Not existent in Java.
print [x] or [y]
print type([x] or [y])

## Ternary conditional operator
print x if x < y else y
