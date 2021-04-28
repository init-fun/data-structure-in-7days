class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data) -> None:
        self.root = Node(data)
            self.root = Node(data)
            return
        return self._insertNew(self.root, data)

    def _insertNew(self, cnode, data):
        if cnode is None:
            cnode = Node(data)
            return
        elif data < cnode.data:  # move to the left
            return self._insertNew(cnode.left, data)
        elif data > cnode.data:
            return self._insertNew(cnode.right, data)
        else:
            # duplicate entry
            print("Duplicate entry")
            return

    def search(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        return self._searchThis(self.root, data)

    def _serachThis(self, cnode, data):
        if cnode.data == data:
            print("Found")
            return True
        elif data < cnode.data:
            return self._serachThis(cnode.left, data)
        elif data > cnode.data:
            return self._serachThis(cnode.right, data)
        else:
            print("eleement not found")
            return False

    def delete(self, data):
        return self._delete_this(self.root, data)

    def _delete_this(self, cnode, data):
        if cnode is None:
            print("Not found")
            return

        if data < cnode.data:  # move to the left
            cnode.left = self._delete_this(cnode.left, data)
        elif data > cnode.data:  # move to the right
            cnode.right = self._delete_this(cnode.right, data)
        else:
            # found it
            if cnode.right and cnode.left:
                # find successor
                # copy the succ(tmp) to cnode
                # delete the succ node
                tmp = cnode.right
                while tmp.left:
                    tmp = tmp.left
                cnode.data = tmp.data

                # now delete the succ node
                cnode.right = self._delete_this(cnode.right, tmp.data)
            else:
                if cnode.left:
                    tmp = cnode.left

                else:
                    tmp = cnode.right

            cnode = tmp
            return cnode
