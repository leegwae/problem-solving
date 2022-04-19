class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initializes the object with the size of the queue to be k
        :param int k: size of the queue
        """
        self.arr = [None] * (k + 1)
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. Return true if the operation is successful.
        :param int value: element to insert
        :return: true if the operation is successful
        """
        isFull = self.isFull()
        if not isFull:
            self.arr[(self.rear + 1) % len(self.arr)] = value
            self.rear = (self.rear + 1) % len(self.arr)

        return not isFull

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. Return true if the operation is successful.
        :return: true if the operation is successful
        """
        isEmpty = self.isEmpty()
        if not isEmpty:
            self.arr[(self.front + 1) % len(self.arr)] = None
            self.front = (self.front + 1) % len(self.arr)

        return not isEmpty

    def Front(self) -> int:
        """
        Gets the front item from the queue. If the queue is empty, return -1.
        :return: element at the front
        """

        if self.isEmpty():
            return -1
        else:
            return self.arr[(self.front + 1) % len(self.arr)]

    def Rear(self) -> int:
        """
        Gets the last item from the queue. If the queue is empty, return -1.
        :return: element at the last
        """

        if self.isEmpty():
            return -1
        else:
            return self.arr[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        :return: true if queue is empty
        """

        return self.rear == self.front

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        :return: true if queue is full
        """

        return (self.rear + 1) % len(self.arr) == self.front
