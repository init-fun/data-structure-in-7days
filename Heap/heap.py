class Heap:
    def __init__(self, max_size=10):
        self.heap = [None] * max_size
        self.count = 0
        self.heap[0] = 99999

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, data):
        if self.is_empty():
            self.heap[1] = data
            self.count += 1
            return
        self.count += 1
        self.heap[self.count] = data
        self.restore_up(self.count)
        return

    def restore_up(self, pos):
        cnode = self.heap[pos]
        parent = pos // 2
        while self.heap[parent] < cnode:
            self.heap[pos] = self.heap[parent]
            pos = parent
            parent = pos // 2
        self.heap[pos] = cnode
        return

    def delete_root(self):
        if self.count == 0:
            print("Heap is empty")
            return
        max_val = self.heap[1]  # store max val node
        self.heap[1] = self.heap[self.count]  # copy the last node to the root
        self.count -= 1  # decrease the length by 1
        self.restore_down(1)  # do the restore down until
        # both child are small or leaf nodeis reached
        return max_val

    def restore_down(self, pos):
        cnode = self.head[pos]  # store the max val
        left_child = 2 * pos
        right_child = left_child + 1

        while right_child <= self.count:
            if cnode >= self.heap[left_child] and cnode >= self.heap[right_child]:
                self.heap[pos] = cnode
                return
            else:
                if self.heap[left_child] > self.heap[right_child]:
                    self.heap[pos] = self.heap[left_child]
                    pos = left_child
                else:
                    self.heap[pos] = self.heap[right_child]
                    pos = right_child

            left_child = 2 * pos
            right_child = left_child + 1

        if left_child == self.count and cnode < self.heap[left_child]:
            self.heap[pos] = self.heap[left_child]
            pos = left_child
        self.heap[pos] = cnode
        return
