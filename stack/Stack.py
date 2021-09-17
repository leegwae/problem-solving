class Node:
    def __init__(self, item=0, next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        if self.last is None:
            return None

        item = self.last.item
        self.last = self.last.next
        return item