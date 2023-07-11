from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next

        pre_head = ListNode(next=head)
        p0 = pre_head
        pre = None
        cur = p0.next

        for _ in range(cnt // k):
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return pre_head.next


def test_reverse_k_group():
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
        solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)) == [2, 1, 4, 3,
                                                                                                        5], 'wrong result'
    assert print_link_list(
        solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)) == [3, 2, 1, 4,
                                                                                                        5], 'wrong result'


if __name__ == '__main__':
    test_reverse_k_group()
