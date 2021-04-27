class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class CompleteBinaryTree:
    def __init__(self, data=None):
        self.root = Node(data)
        return

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        if self.root.left is None:
            self.root.left = Node(data)
            return
        if self.root.left and self.root.right is None:
            self.root.right = Node(data)
            return

        if self.root.left and self.root.right:
            left_sub = self.root.left
            right_sub = self.root.right
            if left_sub.left is None:
                return self.insert(left_sub)

            if (left_sub.left and left_sub.right) and (right_sub.left is None):
                return self.insert(right_sub)

    def inorder(self):
        if self.root is None:
            print("Empty tree")
            return

        return self._inorderTraversal(self.root, result="")

    def _inorderTraversal(self, cnode, result):
        if cnode:
            result = self._inorderTraversal(cnode.left, result)
            result += str(cnode.data) + "-"
            result = self._inorderTraversal(cnode.left, result)

        return result


tree = CompleteBinaryTree()
# tree.insert(1)
print(tree.inorder())