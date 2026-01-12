from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_link_list(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        l1 = reverse_link_list(l1)
        l2 = reverse_link_list(l2)

        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
            if l2:
                carry += l2.val
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return reverse_link_list(dummy.next)


def test_add_two_numbers():
    def print_link_list(head: Optional[ListNode]):
        if not head:
            return []
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_link_list(solution.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))),
                                                  ListNode(5, ListNode(6, ListNode(4))))) == [7, 8, 0, 7]
    assert print_link_list(
        solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))) == [8, 0,
                                                                                                                  7]
    assert print_link_list(solution.addTwoNumbers(ListNode(0), ListNode(0))) == [0]


if __name__ == '__main__':
    test_add_two_numbers()
