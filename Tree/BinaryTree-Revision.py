from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)
        return

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            print("Underflow")
            return
        popped = self.queue.popleft()
        return popped

    def __len__(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        return

    def pop(self):
        if self.is_empty():
            print("Underflow")
            return
        popped = self.stack.pop()
        return popped

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]


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

    def postorder(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._postorder(self.root, "")

    def _postorder(self, cnode, result=""):
        if cnode:
            result = self._postorder(cnode.left, result)
            result = self._postorder(cnode.right, result)
            result += str(cnode.data) + "-"
        return result

    def preorder(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self._preorder(self.root, "")

    def _preorder(self, cnode, result=""):
        if cnode:
            result += str(cnode.data) + "-"
            result = self._preorder(cnode.left, result)
            result = self._preorder(cnode.right, result)
        return result

    def levelorder(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._levelorder(self.root)

    def _levelorder(self, cnode):
        if self.root is None:
            print("Empty tree ")
            return

        queue = Queue()
        queue.enqueue(cnode)
        result = ""

        while len(queue) > 0:
            result += str(queue.peek().data) + "-"
            cnode = queue.dequeue()
            if cnode.left:
                queue.enqueue(cnode.left)

            if cnode.right:
                queue.enqueue(cnode.right)
        return result

    def revese_level(self):
        if self.root is None:
            print("Empty tree")
            return

        return self._reverse_level(self.root)

    def _reverse_level(self, cnode):

        stack = Stack()
        queue = Queue()
        result = ""

        queue.enqueue(cnode)
        while len(queue) > 0:
            popped = queue.dequeue()
            stack.push(popped)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

        while len(stack) > 0:
            result += str(stack.pop().data) + "-"

        return result

    def size(self):
        if self.root is None:
            return 0
        return self._treeSize(self.root)

    def _treeSize(self, cnode):
        cnode = self.root
        stack = Stack()
        stack.push(cnode)
        total = 1
        while stack:
            cnode = stack.pop()
            if cnode.left:
                total += 1
                stack.push(cnode.left)
            if cnode.right:
                total += 1
                stack.push(cnode.right)

        return total

    def height(self, root):
        if root is None:
            return -1

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)


bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.left.left = Node(3)
bt.root.left.right = Node(4)
bt.root.left.right.left = Node(5)
bt.root.right = Node(6)
bt.root.right.left = Node(7)
bt.root.right.right = Node(8)
bt.root.right.right.left = Node(9)

print("Inorder:, ", bt.inorder())
print("Postorder:, ", bt.postorder())
print("Preorder: ", bt.preorder())
print("Level order: ", bt.levelorder())
print("Reverse Level order: ", bt.revese_level())
print("Height: ", bt.height(bt.root))
