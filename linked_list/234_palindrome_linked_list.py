import collections
from typing import Deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # using slicing
    # def isPalindrome(self, head: ListNode) -> bool:
    #     if not head:
    #         return False
    #
    #     l = []
    #     node = head
    #     while node is not None:
    #         l.append(node.val)
    #         node = node.next
    #
    #     size = len(l)
    #     for i in range(0, int(size / 2)):
    #         if not l[i] == l[-(i + 1)]:
    #             return False
    #
    #     return True

    # using queue
    # def isPalindrome(self, head: ListNode) -> bool:
    #     if not head:
    #         return False
    #
    #     l = []
    #     node = head
    #     while node is not None:
    #         l.append(node.val)
    #         node = node.next
    #
    #     while len(l) > 1:
    #         if not l.pop(0) == l.pop():
    #             return False
    #
    #     return True

    # using deque
    # def isPalindrome(self, head: ListNode) -> bool:
    #     if not head:
    #         return False
    #
    #     dq: Deque = collections.deque()
    #     node = head
    #     while node is not None:
    #         dq.append(node.val)
    #         node = node.next
    #
    #     while len(dq) > 1:
    #         if not dq.popleft() == dq.pop():
    #             return False
    #
    #     return True

    # using runner
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

if __name__ == "__main__":
    s = Solution()
    head = [1, 2, 2, 1]
    print(s.isPalindrome(head))