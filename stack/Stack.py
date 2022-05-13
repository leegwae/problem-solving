from typing import Optional, TypeVar

T = TypeVar('T')


class ListNode:
	def __init__(self, val: T, next: Optional['ListNode'] = None):
		self.val = val
		self.next = next


class Stack:
	def __init__(self):
		self.top = None

	def is_empty(self) -> bool:
		return self.top is None

	def push(self, item: T):
		self.top = ListNode(item, self.top)

	def pop(self) -> Optional[T]:
		if self.is_empty():
			return None

		val = self.top.val
		self.top = self.top.next

		return val

	def peek(self) -> Optional[T]:
		return None if self.is_empty() else self.top.val
