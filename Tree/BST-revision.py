class Stack:
    def __init__(self):
        self.stack = []
        return

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        return

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        popped = self.stack.pop()
        return popped

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data=None):
        self.root = Node(data)
        return

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
            return
        return self._insert_node(self.root, data)

    def _insert_node(self, cnode, data):
        if data < cnode.data:
            # insert to the left of the tree
            if cnode.left is None:
                cnode.left = Node(data)
            else:
                return self._insert_node(cnode.left, data)

        if data > cnode.data:
            # insert to the right ot the tree
            if cnode.right is None:
                cnode.right = Node(data)
                return
            else:
                return self._insert_node(cnode.right, data)

        if data == cnode.data:
            print("Duplicate entry")
            return

    def inorder(self):
        if self.root is None:
            print("Empty tree")
            return

        return self._inorder(self.root, "")

    def _inorder(self, cnode, result):
        if cnode:
            result = self._inorder(cnode.left, result)
            result += str(cnode.data) + "-"
            result = self._inorder(cnode.right, result)
        return result

    def search(self, data):
        if self.root is None:
            print("Empty tree")
            return
        return self._search(self.root, data)

    def _search(self, cnode, data):
        if cnode.data == data:
            return True

        if data < cnode.data:
            # might be on the left side for sure
            if cnode.left is not None:
                if cnode.left.data == data:
                    return True
                else:
                    return self._search(cnode.left, data)
            else:
                return False

        if data > cnode.data:
            # might be on the right side for sure
            if cnode.right is not None:
                if cnode.right.data == data:
                    return True
                else:
                    return self._search(cnode.right, data)
            else:
                return False

    def is_BST(self):
        if self.root is None:
            return True

        bst_flag = self._is_it_bst(self.root, self.root.data)
        if bst_flag is None:
            return True

        return False

    def _is_it_bst(self, cnode, data):
        # check if the LEFT < ROOT < RIGHT
        if cnode.left:
            if cnode.left.data < data:
                return self._is_it_bst(cnode.left, cnode.left.data)
            else:
                return False

        if cnode.right:
            if cnode.right.data < data:
                return self._is_it_bst(cnode.right, cnode.right.data)
            else:
                return False

    def minimum(self):
        if self.root is None:
            print("Empty tree")
            return
        cnode = self.root
        while cnode.left:
            cnode = cnode.left
        return cnode.data

    def maximum(self):
        if self.root is None:
            print("Empty tree")
            return
        cnode = self.root
        while cnode.right:
            cnode = cnode.right
        return cnode.data

    def min2(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._min2(self.root)

    def _min2(self, cnode):
        if cnode.left is None:
            return cnode.data
        return self._min2(cnode.left)

    def max2(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._max2(self.root)

    def _max2(self, cnode):
        if cnode.right is None:
            return cnode.data
        return self._max2(cnode.right)


bst = BST(20)
bst.insert(8)
bst.insert(5)
bst.insert(9)
bst.insert(10)
bst.insert(24)
bst.insert(22)
bst.insert(25)
bst.insert(21)
bst.insert(23)
print("Inorder: ", bst.inorder())
print("BST has 99: ", bst.search(99))
print("BST has 10: ", bst.search(10))
print("BST check: ", bst.is_BST())
print("Min Node: ", bst.minimum())
print("Max Node: ", bst.maximum())
print("Min2 Node: ", bst.min2())
print("Max2 Node: ", bst.max2())
