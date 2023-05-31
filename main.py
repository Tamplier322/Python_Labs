from Serializers.ser_factory import SerializersFactory, SerializerType
import math


def my_decor(meth):
    def inner(*args, **kwargs):
        print('NOW WE ARE IN DECORATOR')
        return meth(*args, **kwargs)

    return inner


class First:
    x = 123
    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 111222333

    def __str__(self):
        return 'THIS IS CLASS FIRST11'

    def __repr__(self):
        return 'THIS IS CLASS FIRST22'


class Second:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def class_meth(cls):
        return math.pi


class Third(First, Second):
    pass


ser = SerializersFactory.create_serializer(SerializerType.JSON)

Third_ser = ser.dumps(Third)
Third_des = ser.loads(Third_ser)

third = Third(1, 2)
third_ser = ser.dumps(third)
third_des = ser.loads(third_ser)

print(third_des)
print("this is x in first class: ", third_des.x)
print(third_des.my_sin(10))
print(Third_des.stat())
print(third_des.class_meth())