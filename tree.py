class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<<{self.data}>>"


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return self
                node = current.left
                return node

            else:
                if current.right is None:
                    current.right = node
                    return self
                node = current.right
                return node


    def remove_new(self,value):
        def remove_node(node, value):
            if node is None:
                return None

            if value < node.value:
                node.left = remove_node(node.left,value)
                return node
            elif value > node.value:
                node.right = remove_node(node.right,value)
                return node
            else:
                if node.left is None: # Node with left child None
                    return node
                elif node.right is None: # Node with right child None
                    return node
                else:                   # Node with 2 Child
                    temp_node = node.right
                    print(temp_node.value)
                    while temp_node.left is not None:
                        temp_node = temp_node.left
                    node.value = temp_node.value
                    node.right = remove_node(node.right,temp_node.value)
                return node
        self.root = remove_node(self.root,value)



bst = BinaryTree()
bst.insert(10)
bst.insert(30)
bst.insert(9)
bst.insert(20)
bst.insert(15)
bst.insert(5)
bst.insert(8)
bst.remove_new(10)
