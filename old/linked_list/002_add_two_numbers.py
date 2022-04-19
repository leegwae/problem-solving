from typing import Optional
from ListNode import ListNode, createLinkedList, printNodes

class Solution:
    # l1에 계산 결과를 저장한다.
    # 따라서 l1이 l2보다 노드가 더 많으면 l2의 순회가 끝난 시점에서 루프를 종료한다.
    # l2
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     # 순회용 노드
    #     temp = l1
    #
    #     while temp and l2:
    #         sum = temp.val + l2.val
    #         remainder = sum % 10
    #         temp.val = remainder
    #         if sum >= 10:
    #             if l2.next:
    #                 l2.next.val += 1
    #             else:
    #                 l2.next = ListNode(1)
    #
    #         if temp.next and not l2.next:
    #             break
    #         elif not temp.next and l2.next:
    #             temp.next = ListNode()
    #
    #         temp = temp.next
    #         l2 = l2.next
    #
    #     return l1

    # 위 코드 개선
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 순회용 노드
        temp = l1

        while temp and l2:
            carry, remainder = divmod(temp.val + l2.val, 10)
            temp.val = remainder

            if carry:
                if l2.next:
                    l2.next.val += carry
                else:
                    l2.next = ListNode(carry)

            if temp.next and not l2.next:
                break
            elif not temp.next and l2.next:
                temp.next = ListNode()

            temp = temp.next
            l2 = l2.next

        return l1


    # 전가산기 구조 이용
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     root = head = ListNode(0)
    #
    #     # carry digit(자리올림수)
    #     carry = 0
    #     while l1 or l2 or carry:
    #         if l1:
    #             carry += l1.val
    #             l1 = l1.next
    #
    #         if l2:
    #             carry += l2.val
    #             l2 = l2.next
    #
    #         carry, remainder = divmod(carry, 10)
    #         head.next = ListNode(remainder)
    #         head = head.next
    #
    #     return root.next


if __name__ == '__main__':
    s = Solution()
    l1 = createLinkedList([9,9,9,9,9,9,9])
    l2 = createLinkedList([9,9,9,9])
    added = s.addTwoNumbers(l2, l1)
    printNodes(added)