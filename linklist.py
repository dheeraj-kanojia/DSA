class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<<< your head {self.head}>>"

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
            current = current.next



    def insert_at(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            if self.tail is None:
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


    def remove_at(self, index,data):
        node = Node(data)
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            previous = None
            i = 0
            while i < index and current is not None:
                previous = current
                current = current.next
                i += 1

            if current is None:
                raise IndexError("Does not have any condition")
            previous.next = current.next
            if node.next is None:
                self.tail = previous


    def remove_at_index(self,index):

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            previous = None
            i = 0
            while i < index and current is not None:
                previous = current
                current = current.next
                i += 1
            if current is None:
                raise IndexError("Data Not available")
            previous.next = current.next
            if previous.next is None:
                self.tail = previous

    def get_value(self,index):
        current = self.head
        i = 0
        while i < index and current is not None:
            current = current.next
            i += 1
        if current is not None:
            return current.data
        else:
            return IndexError("Data Issue")





class double_node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.data}"


class double_linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = double_node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self,data):
        new_node = double_node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1


    def insert(self,index,data):
        node = double_node(data)

        if index < 0 and self.length > 0:    # check is index is less than 0 and Node is None:
            return None

        if index == 0:
            self.prepend(node)
            return

        if index == self.length:
            self.append(node)
            return

        current = self.head

        for _ in range(index - 1):
            current = current.next

        node.next = current.next
        node.prev = current

        if current.next:
            current.next.prev = node

        current.next = node

        self.length += 1


    def delete_node(self,index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head

            for _ in range(index):
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev

        self.length -= 1
        return True


    def delete_node_new(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.head = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.tail = None
        else:
            current = self.head

            for _ in range(index):
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev

        self.length -= 1
        return True


    def connect_head_tail(self):

        self.head.prev = self.tail.next
        self.tail.next = self.head.prev


    def print_all(self):
        current = self.head
        t = ""
        while current is not None:
            # print(current.data)
            t += "".join(f"-{current.data}")
            current = current.next

        return t


    def print_rev(self):
        current = self.head
        t = ""
        while current is not None:
            current = current.next
            t += "".join(f"-{current}")
        return t
#
#
# l2 = double_linklist()
#
# l2.append(2)
# l2.append(3)
# l2.append(4)
# l2.append(6)
# l2.append(5)
# l2.append(8)
# l2.insert(5,10)
# l2.insert(0,11)
# print(l2.print_all())
# l2.delete_node_new(4)
# l2.connect_head_tail()
# print(l2.print_all())
# print(l2.print_rev())

#
# l1 = linklist()
#
# l1.a(5)
# l1.add(10)
# l1.add(25)
# l1.add(35)
# l1.add(45)
# l1.insert_at(0,4100)
# l1.remove_at_index(1)
# print(l1.get_value(20))

# print(l1.print_all())



