print("Hello world!")

print("Type first number: ")
a = int(input())
print("Type second number: ")
b = int(input())
print("Type operation: ")
oper = input()

def simple_calc(a, b, oper):
    return a+b

simple_calc(a, b, oper)