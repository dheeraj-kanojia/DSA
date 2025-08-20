class Queue():
    def __init__(self):
        self.items = []
        self.front = 0
        self.back = 0

    def is_empty(self):
        return self.front == self.back

    def size(self):
        return self.back - self.front

    def enqueue(self,key):
        self.items.append(key)
        self.back += 1

    def dequeue(self):
        if self.is_empty():
            return self.items[self.front]
        item = self.items[self.front]
        self.front += 1
        return item


    def peek(self):
        if self.is_empty():
            return self.back
        return self.items[self.front]






