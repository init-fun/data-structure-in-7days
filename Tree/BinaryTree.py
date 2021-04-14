class Node:
    def __init__(self, left = None,data, right = None):
        self.data = data
        self.left = left
        self.right = right
    

def inorder(root):
    # traverse left
    inorder(root.left)
