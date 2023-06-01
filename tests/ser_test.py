from Serializers.ser_factory import SerializersFactory, SerializerType
from tests import *

serializer = SerializersFactory.create_serializer(SerializerType.JSON)


def test_simple_1():
    assert a == serializer.loads(serializer.dumps(a))


def test_simple_2():
    assert aa == serializer.loads(serializer.dumps(aa))


def test_simple_3():
    assert b == serializer.loads(serializer.dumps(b))


def test_simple_4():
    assert bb == serializer.loads(serializer.dumps(bb))


def test_simple_5():
    assert c == serializer.loads(serializer.dumps(c))


def test_simple_6():
    assert cc == serializer.loads(serializer.dumps(cc))


def test_simple_7():
    assert d == serializer.loads(serializer.dumps(d))


def test_simple_8():
    assert dd == serializer.loads(serializer.dumps(dd))


def test_simple_9():
    assert e == serializer.loads(serializer.dumps(e))


def test_simple_10():
    assert f == serializer.loads(serializer.dumps(f))


def test_collection_1():
    assert list1 == serializer.loads(serializer.dumps(list1))


def test_collection_2():
    assert list2 == serializer.loads(serializer.dumps(list2))


def test_collection_3():
    assert set1 == serializer.loads(serializer.dumps(set1))


def test_collection_4():
    assert set2 == serializer.loads(serializer.dumps(set2))


def test_collection_5():
    assert tuple1 == serializer.loads(serializer.dumps(tuple1))


def test_collection_6():
    assert tuple2 == serializer.loads(serializer.dumps(tuple2))


def test_collection_7():
    assert bytes1 == serializer.loads(serializer.dumps(bytes1))


def test_collection_8():
    assert dict1 == serializer.loads(serializer.dumps(dict1))


def test_collection_9():
    assert dict2 == serializer.loads(serializer.dumps(dict2))


def test_collection_10():
    assert dict3 == serializer.loads(serializer.dumps(dict3))


def test_func_1():
    assert func1() == serializer.loads(serializer.dumps(func1))()


def test_func_2():
    assert func2(12) == serializer.loads(serializer.dumps(func2))(12)


def test_func_3():
    assert func3(12) == serializer.loads(serializer.dumps(func3))(12)


def test_func_4():
    assert func3(12, 12, 12, 12, 12) == serializer.loads(serializer.dumps(func3))(12, 12, 12, 12, 12)


def test_func_5():
    assert func4(0.5) == serializer.loads(serializer.dumps(func4))(0.5)


def test_func_6():
    assert func5([4, 3, 2, 1]) == serializer.loads(serializer.dumps(func5))([4, 3, 2, 1])


def test_class_1():
    tmp = serializer.loads(serializer.dumps(A))
    tmp = tmp()
    a = A()

    assert a.a == tmp.a
    assert a.qwe(2) == tmp.qwe(2)


def test_class_2():
    tmp = serializer.loads(serializer.dumps(B))
    tmp = tmp(2)
    b = B(2)

    assert tmp.a == b.a
    assert tmp.func() == b.func()
    assert tmp.qwe(4) == b.qwe(4)



def test_class_object_1():
    a = A()
    tmp = serializer.loads(serializer.dumps(a))

    assert tmp.a == a.a
    assert tmp.qwe(4) == a.qwe(4)
