from data_structures.stack.stack import Stack

def test_push_and_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() is None

def test_peek():
    s = Stack()
    s.push(99)
    assert s.peek() == 99
    assert s.pop() == 99
    assert s.peek() is None
