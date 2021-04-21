class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1


class AVLtree:
    def __init__(self, data=None):
        self.cnode = Node(data)

    def inorder(self):
        if self.cnode is None:
            print("Tree is emptrhs")
            return None

        return self._inorder(self.cnode, "")

    def _inorder(self, cnode, result):
        if cnode:
            result = self._inorder(cnode.left, result)
            result += str(cnode.data) + "-"
            result = self._inorder(cnode.right, result)
        return result

    def insert(self, data):
        if self.cnode is None:
            self.cnode = Node(data)
            return

        return self._insert_new_node(self.cnode, data)

    def _insert_new_node(self, cnode, data):
        if data < cnode.left:
            if cnode.left is None:
                cnode.left = Node(data)
                # balance the tree now
            else:
                return self._insert_new_node(cnode.left, data)

        if data > cnode.right:
            if cnode.right is None:
                cnode.right = Node(data)
                # balance the tree now
            else:
                return self._insert_new_node(cnode.right, data)

        cnode.height = 1 + max(self.getHeight(cnode.left), self.getHeight(cnode.right))

        # balance factor
        balanceFactor = self.getBalance(cnode)

        if balanceFactor > 1:
            if data < cnode.left.data:
                return self.rightRotate(cnode)
            else:
                cnode.left = self.leftRotate(cnode.left)
                return self.rightRotate(cnode)

        if balanceFactor < -1:
            if data > cnode.right.data:
                return self.leftRotate(cnode)
            else:
                cnode.right = self.rightRotate(cnode.right)
                return self.leftRotate(cnode)

        return cnode

    def getHeight(self, cnode):
        if cnode is None:
            return 0
        return cnode.height

    def getBalance(self, cnode):
        if cnode is None:
            return 0
        return self.getHeight(cnode.left) - self.getHeight(cnode.right)

    def leftRotate(self, cnode):
        rhs = cnode.right
        lhs = rhs.left

        rhs.left = cnode
        cnode.right = lhs

        cnode.height = 1 + max(self.getHeight(cnode.left), self.getHeight(cnode.right))

        rhs.height = 1 + max(self.getHeight(rhs.left), self.getHeight(rhs.right))
        return rhs

    def delete(self, data):
        if self.cnode is None:
            print("Tree is empty")
            return
        return self._deleteNode(self.cnode, data)

    def _deleteNode(self, cnode, data):
        if cnode is not None:
            return cnode

        elif data < cnode.left:
            cnode.left = self._deleteNode(cnode.left, data)

        elif data > cnode.left:
            cnode.right = self._deleteNode(cnode.right, data)

        # delete the cnode node
        else:
            if cnode.left is None:
                temp = cnode.right
                cnode = None
                return temp

            if cnode.right is None:
                temp = cnode.left
                cnode = None
                return temp

            temp = self.getMinValueNode(cnode.right)
            cnode.data = temp.data
            cnode.right = self._deleteNode(cnode.right, temp.data)

        if cnode is None:
            return cnode

        # Update the balance factor of nodes
        cnode.height = 1 + max(self.getHeight(cnode.left), self.getHeight(cnode.right))

        balanceFactor = self.getBalance(cnode)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(cnode.left) >= 0:
                return self.rightRotate(cnode)
            else:
                cnode.left = self.leftRotate(cnode.left)
                return self.rightRotate(cnode)
        if balanceFactor < -1:
            if self.getBalance(cnode.right) <= 0:
                return self.leftRotate(cnode)
            else:
                cnode.right = self.rightRotate(cnode.right)
                return self.leftRotate(cnode)
        return cnode

    def getMinValueNode(self, cnode):
        if cnode is None or cnode.left is None:
            return cnode
        return self.getMinValueNode(cnode.left)