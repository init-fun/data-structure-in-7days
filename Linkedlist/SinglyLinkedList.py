class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        cnode = self.head
        while cnode:
            print(f"{cnode.data} >", end=" ")
            cnode = cnode.next
        print()
        return

    def insert_at_begining(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        cnode = self.head
        new_node = Node(new_data)
        new_node.next = cnode
        self.head = new_node
        return

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next

        new_node = Node(new_data)
        cnode.next = new_node
        return

    def insert_after(self, data, new_data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next

        if cnode is None:
            print(f"{data} not found")
            return
        else:
            # insert the new node here
            new_node = Node(new_data)
            new_node.next = cnode.next
            cnode.next = new_node
            return

    def insert_before(self, data, new_data):
        if self.head is None:
            print("list is empty")
            return
        cnode = self.head

        # for the single node
        if cnode.data == data and cnode.next is None:
            new_node = Node(new_data)
            new_node.next = cnode
            self.head = new_node
            return

        while cnode.next:
            if cnode.next.data == data:
                break
            cnode = cnode.next
        if cnode.next is None:
            print(f"{data} not found")
            return
        else:
            new_node = Node(new_data)
            new_node.next = cnode.next
            cnode.next = new_node
            return

    def concatenate(self, sec_list):
        if self.head is None:
            self.head = sec_list.head
            return
        if sec_list.head is None:
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = sec_list.head
        return self.head

    def reverse(self):
        if self.head is None:
            return None
        cnode = self.head
        prev_node = None
        while cnode:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node
        self.head = prev_node
        return self.head

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        return

    def delete_end_node(self):
        # no node
        if self.head is None:
            print("list is empty")
            return
        # single node
        if self.head.next is None:
            self.head = None
            return
        cnode = self.head
        while cnode.next.next:
            cnode = cnode.next
        cnode.next = None
        return

    def delete_this(self, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None and self.head.data == data:
            # delete the only node
            self.head = None
            return
        # if the node to be deleted is the very first node
        if self.head.data == data:
            self.delete_first_node()
            return

        # get the ref of the node before the actual node to be deleted
        cnode = self.head
        while cnode.next:
            if cnode.next.data == data:
                break
            cnode = cnode.next
        if cnode is None:
            print(f"{data} not found")
            return
        else:
            cnode.next = cnode.next.next
            return

    def bubble_sort(self):
        if self.head is None:
            print("List is empty")
            return
        end_node = None

        while self.head.next is not end_node:
            cnode = self.head
            while cnode.next is not end_node:
                next_node = cnode.next
                if cnode.data >= next_node.data:
                    # swap the nodes
                    cnode.data, next_node.data = next_node.data, cnode.data
                cnode = cnode.next
            end_node = cnode

    def merge(self, sec_list):
        new_list = SinglyLinkedList()
        new_list.head = self.merge_these_two(self.head, sec_list.head)
        return new_list

    def merge_these_two(self, first, second):
        if first.data <= second.data:
            new_node = Node(first.data)
            first = first.next
        else:
            new_node = Node(second.data)
            second = second.next

        third_list = new_node
        # new_list_ref = new_node

        while first and second:
            if first.data <= second.data:
                third_list.next = Node(first.data)
                first = first.next
            else:
                third_list.next = Node(second.data)
                second = second.next
            third_list = third_list.next

        while first:

            third_list.next = Node(first.data)
            first = first.next
            third_list = third_list.next

        while second:
            third_list.next = Node(second.data)
            second = second.next
            third_list = third_list.next

        return new_node


myList = SinglyLinkedList()
# myList.traverse()

myList.insert_at_begining(50)
myList.insert_at_begining(40)
myList.insert_at_begining(30)
myList.insert_at_begining(20)

myList.insert_at_end(60)
myList.insert_at_end(70)
myList.insert_at_end(80)

myList.insert_after(60, 65)
myList.insert_after(80, 85)
myList.insert_after(20, 25)
print("List 1", end=">>> ")
myList.traverse()

myList2 = SinglyLinkedList()
myList2.insert_at_begining(50)
myList2.insert_at_begining(40)
myList2.insert_at_begining(30)
myList2.insert_at_begining(20)
print("List 2", end=">>> ")
myList2.traverse()
print("Adding:", end=">>> ")
myList2.concatenate(myList)
myList2.traverse()

myList2.reverse()
print("Reversing ", end=">>> ")
myList2.traverse()

# new list
myList3 = SinglyLinkedList()
myList3.insert_at_begining(50)
myList3.insert_at_begining(40)
myList3.insert_at_begining(30)
myList3.insert_at_begining(20)
print("List 3:", end=">>> ")
myList3.traverse()

myList3.insert_after(50, 55)
myList3.delete_this(20)
myList3.delete_this(40)
myList3.delete_this(55)
print("This is the state of each of the list at this moment")

print("Bubble sort")
myList2.traverse()
myList2.bubble_sort()
myList2.traverse()

print()
print("Merging two list")
myList.traverse()
myList3.traverse()

# new_list = myList.merge_them(myList3)
new_list = myList.merge(myList3)
new_list.traverse()
