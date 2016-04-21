## SHALLOW COPY

person = ["name", ["savings", 100.00]]
print id(person), id(person[:])
print "---- Slice copy"
husband = person[:]
print id(person), id(person[:])
print id(person), id(husband)
# They both refer to the same string "name" as their first element and so on.
print "id() of names:", id(person[0]), id(husband[0])
print "id() of savings:", id(person[1]), id(husband[1])
husband[0] = "isa"
print person, "\n", husband

print "---- Factory function copy"
wife = list(person)
wife[0] = "hilal"                   # Assign new object, so one change cannot effect other. No magic
print id(person), id(person[:])
print id(person), id(wife)
print "---- All three\n", id(person), id(husband), id(wife)
print person, "\n", husband, "\n", wife

## Notes till now:
# We have shallow copies. Only references are copied for the inner objects, not the object itself.
# The object copied itself is new, but the contents are not.
# Lets see what this means.
husband[1][1] = 50.00               # Assign new value to the state of aliased object. This is state modification for aliased object, not a new object assignment.
print person, "\n", husband, "\n", wife  # This line has changed inner list in all 3 objects. All are mutated.

