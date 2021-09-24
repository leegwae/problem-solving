from typing import List, Optional
from ListNode import ListNode, createLinkedList, printNodes

class Solution:
    # using iteration
    # def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     head = node = ListNode(None)
    #
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             node.next = l1
    #             node = node.next
    #
    #             l1 = l1.next
    #         else:
    #             node.next = l2
    #             node = node.next
    #
    #             l2 = l2.next
    #
    #     if l1 or l2:
    #         node.next = l1 or l2
    #
    #     return head.next

    # recursion
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1에 노드가 없거나
        # (l1에 노드가 있고) l2에 노드가 있고 l1의 첫번째 노드의 값이 l2의 첫번째 노드의 값보다 큰 경우
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


if __name__ == "__main__":
    s = Solution()
    l1 = createLinkedList([1, 2, 4])
    l2 = createLinkedList([1, 3, 4])
    merged = s.mergeTwoLists(l1, l2)
    printNodes(merged)


