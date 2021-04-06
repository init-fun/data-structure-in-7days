class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CyclicLinkedList:
    def __init__(self):
        self.last = None

    def traverse(self):
        if self.last is None:
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

        cnode = self.last.next
        while True:
            if cnode.data == data:
                break
            cnode = cnode.next
            if cnode is self.last.next:
                break

        if cnode is self.last.next and cnode.data != data:
            print(f"{data} not found in the list")
            return
        else:
            new_node = Node(new_data)
            new_node.next = cnode.next
            cnode.next = new_node
            if cnode is self.last:
                self.last = new_node

    def insert_before(self, data, new_data):
        if self.last is None:
            print("List is empty")
            return
        cnode = self.last.next
        prev_node = self.last
        while True:
            if cnode.data == data:
                break
            prev_node = cnode
            cnode = cnode.next
            if cnode is self.last.next:
                break
        if cnode is self.last.next and cnode.data != data:
            print(f"{data} is not present in the lsit")
        else:
            # the ref is on the cnode
            new_node = Node(new_data)
            new_node.next = cnode
            prev_node.next = new_node
            prev_node = new_node
        return

    def delete_begining_node(self):
        if self.last is None:
            print("List is empty")
            return
        if self.last.next is self.last:
            # in case of single node
            self.last = None
            return
        self.last.next = self.last.next.next
        return

    def delete_last_node(self):
        if self.last is None:
            print("List is empty")
            return

        if self.last.next == self.last:
            # single node
            self.last = None
            return

        cnode = self.last.next
        while cnode.next is not self.last:
            cnode = cnode.next
        cnode.next = self.last.next
        self.last = cnode
        return

    def delete_this_node(self, data):
        if self.last is None:
            print("List is empty")
            return
        if self.last.next is self.last:
            self.last = None
            return

        cnode = self.last.next
        while cnode.next is not self.last.next:
            if cnode.next.data == data:
                break
            cnode = cnode.next
        if cnode.next == self.last.next:
            print(f"{data} is not present in the list")
        else:
            cnode.next = cnode.next.next
            if self.last.data == data:
                self.last = cnode
        return