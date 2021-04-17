class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def is_empty(self):
        return self.root == None

    def inorder(self):
        if self.is_empty():
            print("Empty tree")
            return
        cnode = self.root
        return self._inorderTraversal(cnode, "")

    def _inorderTraversal(self, cnode, result=""):
        if cnode:
            result = self._inorderTraversal(cnode.left, result)
            result += str(cnode.data) + "-"
            result = self._inorderTraversal(cnode.right, result)
        return result


bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.left.left = Node(3)
bt.root.left.right = Node(4)
bt.root.left.right.left = Node(5)
bt.root.right = Node(6)
bt.root.right.left = Node(7)
bt.root.right.right = Node(8)
bt.root.right.right.left = Node(9)

print(bt.inorder())