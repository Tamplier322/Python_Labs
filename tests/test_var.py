# simple types
a = -2
b = True
c = 'aaa'
aa = complex(2, 3)
bb = -1.2
cc = ';;;;;;'
d = -10.1
dd = False
e = None
f = 1111

# collection types
dict1 = {4: 2.1, 199: -10}
dict2 = {1: 'aaa', 2: 'bbb'}
dict3 = {(1, (2, (3, (4, (5, (6)))))): (7, (8, (9, (10, (12)))))}
set1 = {1, 2, 3}
set2 = {complex(2, 3), 1, '1', False, -0.551}

list1 = [1, 2]
list2 = [complex(2, 3), 1, 0.9, None]

tuple1 = (1, 2, 3)
tuple2 = (1, '10000000', True, 4, False, False)

bytes1 = bytes([46, 46, 46])

# funcs

def func1():
    return "asdf"


def func2(a):
    return 111 + a * a


def func3(*a):
    sum = 0

    for tmp in a:
        sum = sum + tmp

    return sum

def func4(arr):
    return sorted(arr)


def func5(n):
    if (n == 1):
        return 1
    else:
        return "111"


lambdaA = lambda a: a + 10
lambdaB = lambda a, b, c: a + b + c


# class test

class A:
    a = 4444444

    def __init__(self):
        pass

    def qwe(self, a):
        return a


class B(A):
    c = 333

    def __init__(self, b):
        self.b = b

    def func(self):
        return 11


class E:
    e = 222

    def __init__(self):
        pass

class EE(E):
    ee = 111

    def __init__(self):
        pass

class first:
    def __init__(self):
        pass

    def func(self, a):
        return a
