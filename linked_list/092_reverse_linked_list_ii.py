from ListNode import ListNode, createLinkedList, printNodes
from typing import Optional


class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     root = l = ListNode()
    #     root.next = head
    #     r = None
    #
    #     node = root       # 순회용 노드
    #     currentIndex = 0  # 순회용 노드의 현재 인덱스
    #
    #     while node.next:
    #         if (currentIndex + 1) == left:
    #             l = node
    #         if currentIndex == right:
    #             r = node.next
    #
    #         currentIndex += 1
    #         node = node.next
    #
    #     node = l  # 순회용 노드
    #     tail = r
    #     newNode = None
    #     while node.next and node.next != tail:
    #         newNode = ListNode(node.next.val)
    #         newNode.next = r
    #         r = newNode
    #
    #         node = node.next
    #     l.next = newNode
    #
    #     return root.next

    # using iteration
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if not head or left == right:
    #         return head
    #
    #     root = prev = ListNode(None)
    #     root.next = head
    #     for _ in range(left - 1):
    #         prev = prev.next
    #     start = prev.next
    #
    #     for _ in range(right - left):
    #         temp, prev.next, start.next, = prev.next, start.next, start.next.next
    #         prev.next.next = temp
    #
    #     return root.next

if __name__ == '__main__':
    s = Solution()
    head = createLinkedList([1, 2, 3, 4, 5])
    reversed = s.reverseBetween(head, 1, 2)
    printNodes(reversed)
