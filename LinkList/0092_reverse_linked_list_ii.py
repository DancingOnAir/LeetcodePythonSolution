from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre_head = ListNode(0)
        pre_head.next = head
        p0 = pre_head

        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur
        p0.next = pre
        return pre_head.next


def test_reverse_between():
    def print_link_list(head: Optional[ListNode]):
        if not head:
            return []
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_link_list(
        solution.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)) == [1, 4, 3, 2,
                                                                                                            5], 'wrong result'
    assert print_link_list(solution.reverseBetween(ListNode(5), 1, 1)) == [5], 'wrong result'


if __name__ == '__main__':
    test_reverse_between()
