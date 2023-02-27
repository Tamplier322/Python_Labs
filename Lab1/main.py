#First task (print Hello world)
print("Hello world!")

#Second task (function of simple calculator)
first_number = 4
second_number = 5
operator = "sum"

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

result = simple_calc(first_number, second_number, operator)
print(result)

#Third task (Create list of numbers and return list of even numbers)
list_of_nums = [1, 5, 8, 3, 1, 10, 24234, 43, 235, 2, 0, 0, 4, 1256, 777]
result_of_list = []
def even_in_list(my_list):
    for num in my_list:
        if num % 2 == 0:
            result_of_list.append(num)
        else:
            pass
    return result_of_list

res = even_in_list(list_of_nums)
print(res)
