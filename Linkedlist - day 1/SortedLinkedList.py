class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
        print()
        return

    def insert_in_order(self, new_data):
        new_node = Node(new_data)
        if self.head is None or new_data <= self.data:
            new_node.next = self.head
            self.head = new_node
            return

        cnode = self.head
        while cnode.next and cnode.next.data <= new_data:
            cnode = cnode.next
        new_node.next = cnode.next
        cnode.next = new_node
        return

    def search(self, data):
        if self.head is None:
            print("list is empty")
            return
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == data:
                print(f"{data} found at index {index}")
            if cnode.data > data:
                print(f"{data} not found")
                break
            cnode = cnode.next
            index += 1
