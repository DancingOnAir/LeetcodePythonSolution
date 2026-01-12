from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        p = head
        while p.next:
            p.next, p = ListNode(gcd(p.val, p.next.val), p.next), p.next
        return head

    def insertGreatestCommonDivisors1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        pre = ListNode(0, head)
        while head.next:
            nxt = head.next
            p = ListNode(gcd(head.val, head.next.val), nxt)
            head.next = p
            head = p.next
        return pre.next


def test_insert_greatest_common_divisors():
    solution = Solution()
    head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    head = solution.insertGreatestCommonDivisors(head)
    assert head.val == 18, 'wrong result'
    assert head.next.val == 6, 'wrong result'
    assert head.next.next.val == 6, 'wrong result'
    assert head.next.next.next.val == 2, 'wrong result'
    assert head.next.next.next.next.val == 10, 'wrong result'
    assert head.next.next.next.next.next.val == 1, 'wrong result'
    assert head.next.next.next.next.next.next.val == 3, 'wrong result'


if __name__ == '__main__':
    test_insert_greatest_common_divisors()
