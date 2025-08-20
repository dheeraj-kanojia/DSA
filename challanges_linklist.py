import lib2to3.pgen2.token


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<< Node data = {self.data}"


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None


    def add(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next.next


    def remove_duplicate(self):
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None and next_node.data == current.data:
                next_node = next_node.next
            current.next = next_node
            current = next_node
            print(current)

    def insert_at(self,data,index):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            if self.tail == None:
                self.tail = node
        else:
            current = self.head
            previous = None
            i = 0
            while i < index and current is not None:
                previous = current
                current = current.next
                i += 1
            node.next = current
            if previous is not None:
                previous.next = node
            if node.next is None:
                self.tail = node





l1 = linklist()
l1.add(1)
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(3)
l1.add(4)
l1.add(4)
l1.add(4)
l1.add(5)
l1.print_all()
print(l1.remove_duplicate())