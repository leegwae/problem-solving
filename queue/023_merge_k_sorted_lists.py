from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = node = ListNode(None)
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        while heap:
            item = heapq.heappop(heap)
            idx = item[1]
            node.next = item[2]

            node = node.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return root.next


if __name__ == '__main__':
    s = Solution()
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    merged = s.mergeKLists(lists)

    while merged:
        print(merged.val, end='->')
        merged = merged.next