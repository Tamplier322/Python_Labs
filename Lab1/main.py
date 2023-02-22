#First task (print Hello world)
print("Hello world!")

#Second task (function of simple calculator)
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

#Third task (Create list of numbers and return list of even numbers)
nums = [1, 5, 8, 3, 1, 10, 24234, 43, 235, 2, 0, 0, 4, 1256, 777]
