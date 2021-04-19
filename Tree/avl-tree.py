class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class BinarySeachTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def insert(self, new_data):
        if self.is_empty():
            self.root = Node(new_data)
            return
        self._insert(new_data, self.root)

    def _insert(self, data, cnode):
        if data < cnode.data:
            if cnode.left is None:
                cnode.left = Node(data)
            else:
                self._insert(data, cnode.left)
        elif data > cnode.data:
            if cnode.right is None:
                cnode.right = Node(data)
            else:
                self._insert(data, cnode.right)
        else:
            print("Duplicate entry")
            return

    def search(self, data):
        if self.root is None:
            print("Tree is empty")
            return None

        is_found = self._find(data, self.root)
        if is_found:
            return True
        return False

    def _find(self, data, cnode):
        if data > cnode.data and cnode.right:
            self._find(data, cnode.right)
        elif data < cnode.data and cnode.left:
            self._find(data, cnode.left)
        if data == cnode.data:
            return True

    def inorder(self):
        if self.root:
            res = self._inorder_traversal(self.root, result="")
            print(res)
            return
        return False

    def _inorder_traversal(self, start, result=""):
        if start:
            result = self._inorder_traversal(start.left, result)
            result += str(start.data) + "-"
            result = self._inorder_traversal(start.right, result)
        return result

    def is_bst(self):
        if self.root is None:
            print("tree is empty")
            return True
        is_satisfied = self._is_bst(self.root, self.root.data)
        if is_satisfied is None:
            return True
        return False

    def _is_bst(self, cnode, data):
        if cnode.left:
            if data > cnode.left.data:
                return self._is_bst(cnode.left, cnode.left.data)
            else:
                return False
        if cnode.right:
            if data < cnode.right.data:
                return self._is_bst(cnode.right, cnode.right.data)
            else:
                return False

    # iteratively
    def min_node(self):
        if self.root is None:
            print("Empty tree")
            return
        start = self.root
        while start.left:
            start = start.left
        return start.data

    def max_node(self):
        if self.root is None:
            print("Empty tree")
            return
        start = self.root
        while start.right:
            start = start.right
        return start.data

    # recursively
    def min_node2(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._minimum_node(self.root).data

    def _minimum_node(self, cnode):
        if cnode.left is None:
            return cnode
        return self._minimum_node(cnode.left)

    def max_node2(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._maximum_node(self.root).data

    def _maximum_node(self, cnode):
        if cnode.right is None:
            return cnode
        return self._maximum_node(cnode.right)

    # deletion in BST
    def delete(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        return self._delete_this_node(self.root, data)

    def _delete_this_node(self, cnode, data):
        # find the node to be deleted
        if data < cnode.data:
            cnode.left = self._delete_this_node(cnode.left, data)
        elif data > cnode.data:
            cnode.right = self._delete_this_node(cnode.right, data)
        else:
            # if the node is with only one child or no child
            if cnode.left is None:
                temp = cnode.right
                cnode = None
                return temp
            elif cnode.right is None:
                temp = cnode.left
                cnode = None
                return temp

            # if the node has two children,
            # place the inorder successor in position of the node to be deleted

            temp = self.minValueNode(cnode.right)

            cnode.data = temp.data
            cnode.right = self._delete_this_node(cnode.right, temp.data)
        return cnode

    def minValueNode(self, start):
        while start.left:
            start = start.left
        return start


bst = BinarySeachTree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(10)
bst.insert(15)
bst.insert(1)
bst.insert(3)
bst.insert(7)
bst.inorder()
print("Contain 4: ", bst.search(4))
print("Contain 44: ", bst.search(44))
print("Is it a BST: ", bst.is_bst())
print()
print("Non BST tree")
non_bst = BinarySeachTree()
non_bst.root = Node(5)
non_bst.root.left = Node(55)
non_bst.root.right = Node(1)
non_bst.inorder()
print("Is it a BST: ", non_bst.is_bst())
print()

print("Max and min nodes")

print(bst.min_node())
print(bst.min_node2())

print(bst.max_node())
print(bst.max_node2())

print("Inorder: ")
bst.inorder()
print("Delete 4: ")
bst.delete(4)

# print("Delete 3: ")
# bst.delete(3)

# print("Delete 8: ")
# bst.delete(8)

bst.inorder()