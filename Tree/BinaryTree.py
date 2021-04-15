from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        return self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("underflow")
            return False
        popped = self.stack.pop()
        return popped

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return False
        return self.stack[-1].data


class Queue:
    def __init__(self):
        self.Q = deque()

    def enque(self, data):
        return self.Q.append(data)

    def deque(self):
        if self.is_empty():
            print("Underflow")
            return False
        popped = self.Q.popleft()
        return popped

    def is_empty(self):
        return len(self.Q) == 0

    def peek(self):
        return self.Q[0].data

    def __len__(self):
        return len(self.Q)


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
        elif type == "post":
            return self.postorder(self.root, "")
        elif type == "in":
            return self.inorder(self.root, "")
        elif type == "level":
            return self.level_order(self.root)
        elif type == "reverse_level":
            return self.reverse_level_order(self.root)
        else:
            print("Invalid traversal type")
            return False
        return

    def preorder(self, start, result=""):
        # Root -> left -> right
        if start:
            result += str(start.data) + "-"
            result = self.preorder(start.left, result)
            result = self.preorder(start.right, result)

        return result

    def inorder(self, start, result=""):
        # left -> Root -> Right
        if start:
            result = self.inorder(start.left, result)
            result += str(start.data) + "-"
            result = self.inorder(start.right, result)
        return result

    def postorder(self, start, result=""):
        #  left -> right -> Root
        if start:
            result = self.postorder(start.left, result)
            result = self.postorder(start.right, result)
            result += str(start.data) + "-"
        return result

    def level_order(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enque(start)
        result = ""

        while len(queue) > 0:
            result += str(queue.peek()) + "-"
            node = queue.deque()
            if node.left:
                queue.enque(node.left)
            if node.right:
                queue.enque(node.right)

        return result

    def reverse_level_order(self, start):
        if start is None:
            return


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)
tree.root.left.right.right = Node(7)


print("Preorder: ", tree.traverse_tree_in("pre"))
print("Inorder: ", tree.traverse_tree_in("in"))
print("Postorder: ", tree.traverse_tree_in("post"))
print("Level order: ", tree.traverse_tree_in("level"))
