from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return max(vals[i] + vals[len(vals) - i - 1] for i in range(len(vals) // 2 + 1))


def test_pair_sum():
    solution = Solution()
    assert solution.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))) == 6, 'wrong result'
    assert solution.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))) == 7, 'wrong result'
    assert solution.pairSum(ListNode(1, ListNode(100000))) == 100001, 'wrong result'


if __name__ == '__main__':
    test_pair_sum()
