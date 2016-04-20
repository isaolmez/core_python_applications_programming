def readInput():
    text = raw_input("Enter the expression: \n")
    return text;


def evaluate(expression):
    print type(expression)
    expression = str(expression)
    parts = expression.split(" ")
    print parts, type(parts)
    x, y = eval(parts[0]), eval(parts[2])
    if isinstance(x, (int, long, float, complex)) and isinstance(y, (int, long, float, complex)):
        x, y = coerce(x, y)
        if parts[1] == "+":
            return x + y
        elif parts[1] == "-":
            return x - y
        elif parts[1] == "*":
            return x * y
        elif parts[1] == "/":
            return x / y
        elif parts[1] == "%":
            return x % y
        elif parts[1] == "**":
            return x ** y
        else:
            return None


# print eval(readInput())
print evaluate("2 / 5.0")