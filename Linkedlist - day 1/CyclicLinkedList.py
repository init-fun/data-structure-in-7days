class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CyclicLinkedList:
    def __init__(self):
        self.last = None

    def traverse(self):
        if self.last == None:
            print("List is empty")
            return

        first_node = self.last.next
        while True:
            print(f"{first_node.data} > ", end=" ")
            first_node = first_node.next
            if first_node == self.last.next:
                break
        print()
        return

    def insert_at_begining(self, new_data):
        if self.last is None:
            self.last = Node(new_data, self.last)
            return
        new_node = Node(new_data)
        new_node.next = self.last.next
        self.last.next = new_node
        return

    def insert_at_end(self, new_data):
        if self.last is None:
            self.last = Node(new_data, self.last)
            return
        new_node = Node(new_data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
        return

    def insert_after(self, data, new_data):
        if self.last is None:
            print("List is empty")
            return
        if self.last.data == data and self.last.next is self.last:
            # single node
            new_node = Node(new_data)
            new_node.next = self.last.next
            self.last = new_node
            return
