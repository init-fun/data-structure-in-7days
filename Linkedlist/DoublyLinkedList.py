class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data} > ", end=" ")
            cnode = cnode.next
        print()
        return

    def insert_at_beginging(self, new_data):
        if self.head is None:
            # list is empty
            self.head = Node(new_data)
            return
        cnode = self.head
        new_node = Node(new_data)

        new_node.next = cnode
        cnode.prev = new_node
        self.head = new_node
        return

    def insert_at_end(self, new_data):
        if self.head is None:
            self.insert_at_beginging(new_data)
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        new_node = Node(new_data)
        new_node.prev = cnode
        cnode.next = new_node
        return

    def insert_before_node(self, data, new_data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        if cnode.data == data:
            # for the very first node
            self.insert_at_beginging(new_data)
            return

        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next

        if cnode is None:
            print(f"{data} is not in  List")
            return
        else:
            new_node = Node(new_data)

            new_node.prev = cnode.prev
            new_node.next = cnode
            cnode.prev.next = new_node
            cnode.prev = new_node
            return

    def insert_after_node(self, data, new_data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next

        if cnode is None:
            print(f"{data} is not present in the list")
            return
        else:
            new_node = Node(new_data)
            new_node.prev = cnode
            new_node.next = cnode.next
            if cnode.next is not None:
                cnode.next.prev = new_node
            cnode.next = new_node

    # deletion functions

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
        return

    def delete_last_node(self):
        if self.head is None:
            print("list is empty")
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.prev.next = None
        return

    def delete_this_node(self, data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        if cnode.data == data:
            self.delete_first_node()
            return

        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next
        if cnode is None:
            print(f"{data} is not present in the list")
            return
        else:
            # node is present in the list
            next_node = cnode.next
            prev_node = cnode.prev
            if next_node is None:
                prev_node.next = None
                return
            prev_node.next = next_node
            next_node.prev = prev_node
            return

    def reverse_it(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            return self.head

        # take ref to both the first and sec nodes
        first_node = self.head
        second_node = first_node.next

        first_node.next = None
        first_node.prev = second_node

        while second_node:
            second_node.prev = second_node.next
            second_node.next = first_node
            # move the ptr to the next nodes
            first_node = second_node
            second_node = second_node.prev

        self.head = first_node


myList = DoublyLinkedList()
myList.traverse()

myList.insert_at_beginging(30)
myList.insert_at_beginging(20)
myList.insert_at_beginging(10)
myList.insert_at_end(50)
myList.insert_at_end(60)
myList.traverse()

myList.insert_before_node(30, 25)
myList.insert_after_node(30, 35)
myList.insert_after_node(10, 15)
myList.traverse()

myList.delete_this_node(10)
myList.delete_this_node(60)
myList.delete_this_node(30)
myList.traverse()
myList.reverse_it()
myList.traverse()
