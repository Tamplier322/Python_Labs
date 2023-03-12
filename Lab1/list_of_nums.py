#Third task (Create list of numbers and return list of even numbers)
def even_in_list(my_list, empty_list):
    for num in my_list:
        if num % 2 == 0:
            empty_list.append(num)
        else:
            pass
    return empty_list

