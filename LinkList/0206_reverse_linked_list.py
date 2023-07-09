from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        return pre


def test_reverse_list():
    solution = Solution()
    assert solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).val == 5, 'wrong result'
    assert solution.reverseList(ListNode(1, ListNode(2))).val == 2, 'wrong result'


if __name__ == '__main__':
    test_reverse_list()
