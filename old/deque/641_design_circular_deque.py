# using list
# class MyCircularDeque:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the deque to be k.
#         """
#         self.arr = [None] * k
#         self.MAX_SIZE = k
#         self.front = 0
#         self.rear = 0
#
#     def insertFront(self, value: int) -> bool:
#         """
#         Adds an item at the front of Deque. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         else:
#             if self.isEmpty():
#                 self.arr[self.front] = value
#             else:
#                 newFront = (self.front - 1) % self.MAX_SIZE
#                 self.arr[newFront] = value
#                 self.front = newFront
#             return True
#
#     def insertLast(self, value: int) -> bool:
#         """
#         Adds an item at the rear of Deque. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         else:
#             if self.isEmpty():
#                 self.arr[self.rear] = value
#             else:
#                 newRear = (self.rear + 1) % self.MAX_SIZE
#                 self.arr[newRear] = value
#                 self.rear = newRear
#             return True
#
#     def deleteFront(self) -> bool:
#         """
#         Deletes an item from the front of Deque. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         else:
#             self.arr[self.front] = None
#
#             if self.front != self.rear:
#                 self.front = (self.front + 1) % self.MAX_SIZE
#             return True
#
#     def deleteLast(self) -> bool:
#         """
#         Deletes an item from the rear of Deque. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         else:
#             self.arr[self.rear] = None
#
#             if self.front != self.rear:
#                 self.rear = (self.rear - 1) % self.MAX_SIZE
#             return True
#
#     def getFront(self) -> int:
#         """
#         Get the front item from the deque.
#         """
#         return -1 if self.isEmpty() else self.arr[self.front]
#
#     def getRear(self) -> int:
#         """
#         Get the last item from the deque.
#         """
#         return -1 if self.isEmpty() else self.arr[self.rear]
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular deque is empty or not.
#         """
#         return self.front == self.rear and self.arr[self.front] is None
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular deque is full or not.
#         """
#         return (self.rear + 1) % self.MAX_SIZE == self.front and self.arr[self.front] is not None

# using doubly linked list
class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            newNode = ListNode(value)
            self.size += 1

            if self.isEmpty():
                self.head = self.tail = newNode
            else:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode

            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            newNode = ListNode(value)
            self.size += 1

            if self.isEmpty():
                self.head = self.tail = newNode
            else:
                newNode.prev = self.tail
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.arr[self.front] = None

            if self.front != self.rear:
                self.front = (self.front + 1) % self.MAX_SIZE
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.arr[self.rear] = None

            if self.front != self.rear:
                self.rear = (self.rear - 1) % self.MAX_SIZE
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.arr[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.arr[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity
