class MinHeap:
    def __init__(self, capacity=10):
        self.heap = [None] * capacity
        self.size = 0
        self.capacity = capacity

    # get the proper index of the node
    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftIndex(self, index):
        return index * 2 + 1

    def getRightIndex(self, index):
        return 2 * index + 2

    # parent index should be >= 0
    # left index and right index should be less than the total capacity of the heap

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightIndex(index) < self.size

    # getting the node based on the index
    def parentNode(self, index):
        return self.heap[self.getParentIndex(index)]

    def leftNode(self, index):
        return self.heap[self.getLeftIndex(index)]

    def rightNode(self, index):
        return self.heap[self.getRightIndex(index)]

    # some more helper functions
    def isFull(self):
        return self.capacity == self.size

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return

    # INSERT NEW NODE

    def insert(self, data):
        if self.isFull():
            print("Heap is full")
            return
        # insert at the last index
        # increase the heap size
        # heapify the tree
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1  # because our heap is 0th indexed
        # check if it has a parent, and parent is more than the child node
        while self.hasParent(index) and self.parentNode(index) > self.heap[index]:
            # if it is then swap them
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def anotherIndexMethod(self, data):
        if self.isFull():
            print("heap is full")
            return
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def anotherHeapifyUpMethod(self, index):
        # index is the last element index in the heap
        if self.hasParent(index) and self.getParentIndex(index) > self.heap[index]:
            # do the swapping
            self.swap(self.getParentIndex(index), index)
            self.anotherHeapifyUpMethod(self.getParentIndex(index))

    def removeMinNode(self):
        if self.size == 0:
            print("Heap is empty")
            return
        # min node is always at root
        data = self.heap[0]
        # replace it with the last element of the heap
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown()

    def heapifyDown(self):
        # index = 0  # always start from the root
        # if self.hasRightChild(index) and self.hasLeftChild(index):
        #     # move the min of two node up
        #     min_node = min(self.leftNode(index), self.rightNode(index))
        #     self.swap(min_node, self.parent(index))

        # if self.hasRightChild(index) and not self.hasLeftChild(index):
        #     self.swap(self.getRightIndex(index), self.parentNode(index))

        # if self.hasLeftChild(index) and not self.hasRightChild(index):
        #     self.swap(self.getLeftIndex(index), self.parentNode(index))

        # return
        pass


# https://www.youtube.com/watch?v=hkyzcLkmoBY