from data_structures.arrays.array import DynamicArray

def test_push_and_get():
    arr = DynamicArray()
    arr.push(10)
    arr.push(20)
    arr.push(30)
    assert arr.get(0) == 10
    assert arr.get(1) == 20
    assert arr.get(2) == 30

def test_dynamic_resize():
    arr = DynamicArray()
    for i in range(50):
        arr.push(i)
    assert arr.length == 50
    assert arr.get(49) == 49

def test_pop():
    arr = DynamicArray()
    arr.push(5)
    arr.push(6)
    assert arr.pop() == 6
    assert arr.pop() == 5
    assert arr.pop() is None  # popping empty
