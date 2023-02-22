print("Hello world!")

print("Type first number: ")
a = int(input())
print("Type second number: ")
b = int(input())
print("Type operation: ")
c = input()

def simple_calc(first, second, operation):
    if (operation == "sum"):
        return first + second
    elif (operation == "sub"):
        return first - second
    elif (operation == "mult"):
        return first * second
    elif (operation == "div"):
        return first / second
    else:
        return first

result = simple_calc(a, b, c)
print(result)