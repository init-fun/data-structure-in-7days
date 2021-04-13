class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def is_empty(self):
        return self.head == None

    def size(self):
        print("Size: ", self.q_size)

    def enque(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.q_size += 1
        return

    def deque(self):
        if self.is_empty():
            print("Underflow: Q is empty")
            return
        popped_item = self.head.data
        self.head = self.head.next
        self.q_size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Q is empty")
            return
        return self.head.data

    def display(self):
        if self.is_empty():
            print("Q is empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
        print()
        return
