from typing import List, Optional, TypeVar

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


T = TypeVar('T')


def createLinkedList(l: List[T]):
    root = node = ListNode()

    for n in l:
        node.next = ListNode(n)
        node = node.next

    return root.next


def printNodes(head: ListNode):
    if not head:
        print('리스트에 노드가 없습니다.')

    while head:
        print(f'{head.val}', end='->')
        head = head.next
    print('NULL')


def toList(head: Optional[ListNode]):
    l = []

    while head:
        l.append(head.val)
        head = head.next

    return l