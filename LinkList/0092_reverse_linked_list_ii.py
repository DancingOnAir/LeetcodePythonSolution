from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lo, hi, pre = None, None, None
        cur = head
        cnt = 0

        while cur:
            cnt += 1
            if cnt > right:
                break

            nxt = cur.next
            if cnt >= left:
                if cnt == left:
                    lo = pre
                    hi = cur
                cur.next = pre
            pre = cur
            cur = nxt

        if lo:
            lo.next = pre
        if hi:
            hi.next = cur

        return head


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
