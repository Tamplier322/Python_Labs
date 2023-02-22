print("Hello world!")

print("Type first number: ")
a = int(input())
print("Type second number: ")
b = int(input())
print("Type operation: ")
c = input()

def simple_calc(first, second, operation):
    if (operation == "sum"):
        return [first + second, first, second]
    elif (operation == "sub"):
        return [first - second, first, second]
    elif (operation == "mult"):
        return [first * second, first, second]
    elif (operation == "div"):
        return [first / second, first, second]
    else:
        return "Wrong input!"

result = simple_calc(a, b, c)
print(result)