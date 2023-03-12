#Second task (function of simple calculator)
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

