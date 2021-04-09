class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class StackLinkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        if self.head is None:
            return count
        cnode = self.head
        while cnode:
            count += 1
            cnode = cnode.next
        print(f"Total nodes : {count}")
        return

    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return

        new_node = Node(new_data, self.head)
        self.head = new_node
        return

    def pop(self):
        if self.head is None:
            print("Underflow")
            return
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return
        print("peek : ", self.head.data)
        return self.head.data

    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data}", end=" > ")
            cnode = cnode.next
        print()
        return


myStack = StackLinkedlist()
myStack.display()

print(f"Is stack is empty? : {myStack.is_empty()}")

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(7)
myStack.push(8)
myStack.push(9)
myStack.push(10)
myStack.display()

print(f"Popped item : {myStack.pop()}")
myStack.display()

myStack.peek()

myStack.size()

print(f"Is stack is empty? : {myStack.is_empty()}")