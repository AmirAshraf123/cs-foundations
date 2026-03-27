class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.items[self.front]
        self.front += 1

        # Optimization: cleanup when front pointer grows too large
        if self.front > 50:
            self.items = self.items[self.front:]
            self.front = 0

        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.front >= len(self.items)

    def __str__(self):
        return str(self.items[self.front:])
