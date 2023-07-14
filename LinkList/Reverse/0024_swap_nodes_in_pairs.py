from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        pre_head = ListNode(next=head)
        p0 = pre_head
        pre = None
        cur = head

        for _ in range(cnt // 2):
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return pre_head.next


def test_swap_pairs():
    def print_link_list(head: Optional[ListNode]):
        if not head:
            return []
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_link_list(solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))) == [2, 1, 4,
                                                                                                       3], 'wrong result'
    assert print_link_list(solution.swapPairs(None)) == [], 'wrong result'
    assert print_link_list(solution.swapPairs(ListNode(1))) == [1], 'wrong result'


if __name__ == '__main__':
    test_swap_pairs()
