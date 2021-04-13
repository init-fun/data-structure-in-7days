class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.is_empty():
            return 0
        cnode = self.head.next
        count = 0
        while True:
            count += 1
            cnode = cnode.next
            if cnode == self.head.next:
                break
        return count

    def enque(self, new_data):
        if self.is_empty():
            self.head = Node(new_data, self.head)
            return

        new_node = Node(new_data)

        new_node.next = self.head.next
        self.head.next = new_node
        self.head = new_node
        return

    def deque(self):
        if self.is_empty():
            print("Underflow: Q is empty")
            return
        if self.head.next == self.head:
            popped_item = self.head
            self.head = None
        else:
            popped_item = self.head.next
            self.head.next = self.head.next.next
        return popped_item.data

    def peek(self):
        print("seek: ", self.head.next.data)
        return

    def display(self):
        if self.is_empty():
            print("Q is empty")
            return
        cnode = self.head.next
        while True:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
            if cnode == self.head.next:
                break
        return