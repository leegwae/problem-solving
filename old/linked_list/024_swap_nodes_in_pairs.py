from ListNode import ListNode, createLinkedList, printNodes
from typing import Optional

class Solution:
    # 값만 바꾸기
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     node = head
    #
    #     while node and node.next:
    #         node.val, node.next.val = node.next.val, node.val
    #         node = node.next.next
    #     return head

    # using iteration
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     root = prev = ListNode(None)
    #     prev.next = head
    #
    #     while head and head.next:
    #         temp = head.next
    #         head.next = temp.next
    #         temp.next = head
    #
    #         prev.next = temp
    #
    #         head = head.next
    #         prev = prev.next.next
    #     return root.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        return head

if __name__ == '__main__':
    s = Solution()
    head = createLinkedList([1, 2, 3, 4])
    swapped = s.swapPairs(head)
    printNodes(swapped)
    printNodes(head)