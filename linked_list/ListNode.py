from typing import List, Optional, TypeVar

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


T = TypeVar('T')


def createLinkedList(l: List[T]):
    if not l:
        return None

    head = ListNode()
    # 순회용 노드
    temp = head
    for i, n in enumerate(l):
        temp.val = n
        if i != len(l) - 1:
            temp.next = ListNode()
            temp = temp.next

    return head

def printNodes(head: ListNode):
    if not head:
        print('리스트에 노드가 없습니다.')

    while head:
        print(head.val)
        head = head.next

def toList(head: Optional[ListNode]):
    l = []

    while head:
        l.append(head.val)
        head = head.next

    return l

if __name__ == '__main__':
    head = createLinkedList(['a', 1, 3])
    printNodes(head)