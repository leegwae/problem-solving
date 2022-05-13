from typing import Optional, TypeVar

T = TypeVar('T')


class ListNode:
	def __init__(self, val: T, next: Optional['ListNode'] = None):
		self.val = val
		self.next = next


class Queue:
	def __init__(self):
		self.front = None
		self.rear = None

	def is_empty(self) -> bool:
		return self.front is None

	def enqueue(self, item: T):
		node = ListNode(item, None)

		if self.is_empty():
			self.front = self.rear = node
		else:
			self.rear.next = node
			self.rear = self.rear.next

	def dequeue(self) -> Optional[T]:
		if self.is_empty():
			return None

		val = self.front.val
		self.front = self.front.next

		return val

	def peek(self) -> Optional[T]:
		return None if self.is_empty() else self.front.val
