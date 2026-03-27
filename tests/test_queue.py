from data_structures.queue.queue import Queue

def test_enqueue_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() is None

def test_peek():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    assert q.peek() == 5
    q.dequeue()
    assert q.peek() == 6
