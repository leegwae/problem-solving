# Definition for singly-linked list.
import collections


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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False

        l = collections.deque()
        node = head
        while node is not None:
            l.append(node.val)
            node = node.next

        while len(l) > 1:
            if not l.popleft() == l.pop():
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    head = [1,2,2,1]
    print(s.isPalindrome(head))