from typing import List, Optional, TypeVar

T = TypeVar('T')


class ListNode:
	def __init__(self, val: Optional[T] = None, next: Optional['ListNode'] = None):
		self.val = val
		self.next = next


class Stack:
	def __init__(self):
		self.top = None

	def is_empty(self):
		return self.top is None

	def push(self, item: T):
		self.top = ListNode(item, self.top)

	def pop(self):
		if self.is_empty():
			return None

		val = self.top.val
		self.top = self.top.next

		return val

	def peek(self):
		return None if self.is_empty() else self.top.val
