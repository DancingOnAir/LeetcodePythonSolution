from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # linklist operation
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            p = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = p
                p = cur
                cur = nxt
            return p

        def double(node):
            cur = dummy = ListNode()
            carry = 0
            while node or carry:
                if node:
                    carry += node.val * 2
                cur.next = ListNode(carry % 10)
                carry //= 10
                cur = cur.next
                if node:
                    node = node.next
            return dummy.next

        head = reverse(head)
        res = double(head)
        return reverse(res)

    # math
    def doubleIt1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)

        cur = head
        while cur:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head


def test_double_it():
    solution = Solution()
    head = ListNode(1, ListNode(8, ListNode(9)))
    head = solution.doubleIt(head)
    assert head.val == 3, 'wrong result'
    assert head.next.val == 7, 'wrong result'
    assert head.next.next.val == 8, 'wrong result'

    head = ListNode(9, ListNode(9, ListNode(9)))
    head = solution.doubleIt(head)
    assert head.val == 1, 'wrong result'
    assert head.next.val == 9, 'wrong result'
    assert head.next.next.val == 9, 'wrong result'
    assert head.next.next.next.val == 8, 'wrong result'


if __name__ == '__main__':
    test_double_it()
