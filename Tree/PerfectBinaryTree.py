class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class PerfectBinaryTree:
    def __init__(self, data=None) -> None:
        self.root = Node(data)
        return

    def isPerfect(self):
        if self.root is None:
            return True

        if self.left and self.right:
            depth = 0
            left = self._perfectCheck(self.left, depth)
            right = self._perfectCheck(self.right, depth)

            if left == right:
                return True

        return False

    def _perfectCheck(self, cnode, depth):
        if cnode.left is None and cnode.right is None:
            return depth + 1
        if cnode.left is None and cnode.right is not None:
            return False
        if cnode.left and cnode.right is None:
            return False
        if cnode.left and cnode.right:
            depth += 1
            left_tree = self._perfectCheck(cnode.left, depth)
            right_tree = self._perfectCheck(cnode.right, depth)

            if left_tree == right_tree:
                return depth + 1


new_tree = PerfectBinaryTree()
new_tree.root = Node(1)
new_tree.left = Node(2)
new_tree.right = Node(3)

new_tree.left.left = Node(4)
new_tree.left.right = Node(5)

new_tree.right.left = Node(4)
new_tree.right.right = Node(5)
print(new_tree.isPerfect())
