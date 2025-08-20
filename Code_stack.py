
class stack():

    def __init__(self,limit=14):
        self.stack = []
        self.max_size = 14

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size - 1

    def push(self,key):
        if self.is_full():
            return self.stack
        return self.stack.append(key)

    def pop(self):
        if self.is_full():
            return self.stack
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return IndexError("Peek is empty")
        return self.stack[-1]

    def __str__(self):
        if self.is_empty():
            return f"<Stack empty>"
        return f"<Stack top={self.peek()} | items={self.stack}>"


class Queue:
    def __init__(self):
        self.max_size = 100
        self.head = 0
        self.tail = 0
        self.queue = [None] * 10

    def get_length(self):
        return self.tail - self.head

    def is_empty(self):
        return self.get_length() == 0

    def is_full(self):
        return self.get_length() == self.max_size

    def enqueue(self,key):
        if self.is_full():
            return False
        self.queue[self.tail] = key
        self.tail += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return True
        item = self.queue[self.head]
        self.head += 1
        return item

    def peek(self):
        if self.is_empty():
            return False
        return self.queue[self.head]

    def top(self):
        if self.is_empty():
            return False
        return self.queue[0]

    def pop(self):
        if self.is_full():
            return self.queue
        return self.queue.pop()


s = stack()
q = Queue()


def string_rev_using_stack():
    t = "rattle"
    u = ""
    for i in t:
        s.push(i)

    print(s.stack)

    while s.stack:
        u += "".join(s.pop())

    return u


# string_rev_using_stack()



def imp_st_qu():
    s = "nandos"
    t = ""

    for i in s:
        q.enqueue(i)

    while q.queue:
        p = q.pop()
        if p is not None:
            t += "".join(p)
    print(t)


# imp_st_qu()







