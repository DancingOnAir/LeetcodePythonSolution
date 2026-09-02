from typing import Optional
from itertools import pairwise

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next:
            return [-1,-1]

        res = []
        pre = None
        i = 0
        while head.next:
            if pre:
                if (pre.val < head.val and head.next.val < head.val) or (pre.val > head.val and head.next.val > head.val):
                    res.append(i)
            pre = head
            head = head.next
            i += 1

        if len(res) < 2:
            return [-1,-1]
        return [min(b - a for a, b in pairwise(res)), res[-1] - res[0]]


def test_nodes_between_critical_points():
    solution = Solution()
    # assert solution.nodesBetweenCriticalPoints(ListNode(3, ListNode(1))) == [-1,-1], 'wrong result'
    assert solution.nodesBetweenCriticalPoints(ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))) == [1,3], 'wrong result'
    assert solution.nodesBetweenCriticalPoints(ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))) == [3,3], 'wrong result'


if __name__ == '__main__':
    test_nodes_between_critical_points()
