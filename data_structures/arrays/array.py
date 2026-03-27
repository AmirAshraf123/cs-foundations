class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.data = [None] * self.capacity

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_cap

    def push(self, value):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def pop(self):
        if self.length == 0:
            return None
        value = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return value

    def __str__(self):
        return str([self.data[i] for i in range(self.length)])
