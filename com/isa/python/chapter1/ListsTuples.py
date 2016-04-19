## Non-unique, resizable list
myList = [1, 2, 3, 4, 5, 5]
print myList

## Can contain different types, unlike arrays. Java counterpart is Arraylist, resizable array of objects
customList = ['a', True, 2, 2L]
print customList

## Can reassign values
customList[0] = "b"
print customList

## Can add new values
customList.append(True)
print customList

## Non-unique, readonly, static tuples
myTuples = ("a", 1, 2, 3, True)
print myTuples

## Cannot reassign or append values
# myTuples[0] = "b"
# print myTuples


## Slice access
print customList[0:2]
print myTuples[0:2]

## Pythons Lists conforms the JSON notation of arrays, but Tuples cannot be though as a JSON construct. There are not JSON constructs that includes parantheses.
# But this JSON correlation may not be extended to see Python classes as JSON objects. But for primitive values, it seems work well


## Dictionaries
# Dictionaries, (symbol tables) can also be thought as JSON objects. Java's equavelant is the classes that implement Map interface: HashMap, TreeMap, IdentityHasMap etc.

dictionary = {"name" : "isa", "age":32, "home": "izmir", "name":"isaa"}
print dictionary
print dictionary["name"]
print dictionary["age"]

## Iterate on the keys of dictionary. It seems this map is not sorted, so does not allow ordered operations. And it also does not preserve the insertion order.
## Keys must be unique. If multiple values are specified by the same key, the secondvalue overwrites the previous value, and last value is the final value.
for key in dictionary:
    print key, dictionary[key]