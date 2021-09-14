from ListNode import ListNode, createLinkedList, printNodes
from typing import Optional

class Solution:
    # using recursion
    # def reverseList(self, head: ListNode) -> ListNode:
    #     # prev - node
    #     def reverse(node: ListNode, prev: ListNode = None):
    #         if not node:
    #             return prev
    #
    #         nxt, node.next = node.next, prev
    #         return reverse(nxt, node)
    #
    #     return reverse(head)

    # using iteration
    def reverseList(self, head: ListNode) -> ListNode:
        prev, node = None, head

        while node:
            nxt, node.next = node.next, prev
            prev, node = node, nxt
        return prev

if __name__ == '__main__':
    s = Solution()
    head = createLinkedList([1, 2, 3, 4, 5])
    reversedHead = s.reverseList(head)
    printNodes(reversedHead)