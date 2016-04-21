## DEEP COPY
import copy

person = ["name", ["savings", 100.00]]
print "---- Deep copy husband"
husband = copy.deepcopy(person)
print id(person), id(husband)
# They must refer to different object because of deep copy. Lists are different, but strings are same because of string caching
print "id() of names:", id(person[0]), id(husband[0])
print "id() of savings:", id(person[1]), id(husband[1])
husband[0] = "isa"
print person, "\n", husband

print "---- Deep copy wife"
wife = copy.deepcopy(person)
wife[0] = "hilal"  # Assign new object, so one change cannot effect other. No magic
print id(person), id(wife)
print "---- All three\n", id(person), id(husband), id(wife)
print person, "\n", husband, "\n", wife

## Notes till now:
# The object copied itself is new(new object and new reference variable), also the contents are new.
husband[1][1] = 50.00  # Assign a new value. Since objects are different, they do not affect others
print person, "\n", husband, "\n", wife
