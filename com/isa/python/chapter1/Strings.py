str = "IsaOlmez"
print str[0]
print str[0:1]
print str[0:22]

## Negative indexes start from the end of the string and advances to the start
print str[0:-1]
print str[0:-2]
print str[-1]

## Empty end index, start index advances till the end of string
print str[0:]

## Index advances only from left to right, so negative indexes must also increase in value.
## There is no reverse traversing
print str[-1:-10]
print str[-10:-1]

## Concetanation
print "Concetaneted strings" + ": "
print "isa" + " " + "olmez"

## Escaping made easy.This is what you see in IDE is what you get in the output. Covers all characters that must be escaped.
## Puts newline and other space characters implicitly, to match the editor in IDE.
str = """there is a tree
      there""";
# This is one similar with explicit escapes applied to individual elements. Requires planning.
strAlternative = "there is a tree \n\t\tthere"

strNotAlternative = "there is a tree" \
                    "there"

print str
print strAlternative
print strNotAlternative
