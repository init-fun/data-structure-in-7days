class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CyclicLinkedList:
    def __init__(self):
        self.head = None