class Node:
    def __init__(self, data, next=None, priority=1):
        self.data = data
        self.next = next
        self.priority = priority


class PriorityQue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def enque(self, new_data, pri):
        new_node = Node(new_data, pri)

        # if q is empty OR new node has highest pri
        # insert at the first
        if self.is_empty() or self.pri < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            cnode = self.head
            while cnode.next and cnode.next.priority <= pri:
                cnode = cnode.next
            new_node.next = cnode.next
            cnode.next = new_node
        return

    def deque(self):
        if self.is_empty():
            print("Underflow: Q is empty")
            return
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        cnode = self.head
        while cnode:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
            return
        print()
        return

    def size(self):
        count = 0
        cnode = self.head
        while cnode:
            count += 1
            cnode = cnode.next
        print("Size: ", count)
        return
