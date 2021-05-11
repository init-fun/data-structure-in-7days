class MaxHeap:
    def __init__(self, maxSize=20) -> None:
        self.heap = [None] * maxSize
        self.size = 0

    def inorder(self):
        return self._inorder(self.heap[0], result="")

    def display(self):
        print(self.heap)
        return

    def hasParent(self, index):
        parentIndex = (index - 1) // 2
        if parentIndex >= 0:
            return parentIndex
        return False

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return

    def insert(self, data):
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        parent_node_index = self.hasParent(index)
        if parent_node_index:
            if self.heap[index] > self.heap[parent_node_index]:
                # swapping here
                self.swap(self.heap[parent_node_index], self.heap[index])
                self.heapifyUp(self.heap[parent_node_index])


new_heap = MaxHeap()
for i in [85, 70, 55, 56, 40, 42, 33, 16, 28, 19, 20, 25, 80]:
    new_heap.insert(i)

new_heap.display()