from ListNode import ListNode, createLinkedList, printNodes
from typing import Optional

class Solution:
    # 공간 복잡도 제약을 지키지 않았으므로 잘못된 풀이임
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #
    #     isOdd = False
    #     lastOdd, prev, node = head, head, head.next
    #
    #     while node:
    #         if isOdd:
    #             newOdd = ListNode(node.val)
    #             newOdd.next = lastOdd.next
    #             lastOdd.next = newOdd
    #
    #             lastOdd = newOdd
    #
    #             prev.next = node.next
    #             node = node.next
    #         else:
    #             prev, node = node, node.next
    #         isOdd = not isOdd
    #     return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd, even, even_head = head, head.next, head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head

if __name__ == '__main__':
    s = Solution()
    head = createLinkedList([1,2,3,4,5])
    result = s.oddEvenList(head)
    printNodes(result)