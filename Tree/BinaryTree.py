class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def is_empty(self):
        return self.root == None

    def traverse_tree_in(self, type):
        if type == "pre":
            return self.preorder(self.root, "")
        # elif type == "post":
        #     self.postorder(self.root, "")
        # elif type == "in":
        #     self.inorder(self.root, "")
        else:
            print("Invalid traversal type")
            return False
        return

    def postorder(self, start, result=""):
        #  left -> right -> Root
        if start:
            pass
        return result

    def preorder(self, start, result=""):
        # Root -> left -> right
        if start:
            result += str(start.data) + "-"
            result = self.preorder(start.left, result)
            result = self.preorder(start.right, result)

        return result

    def inorder(self, start, result=""):
        pass


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.right.right.right = Node(7)


print(tree.traverse_tree_in("pre"))
