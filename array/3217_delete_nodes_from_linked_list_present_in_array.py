from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        pre_head = ListNode(0, head)
        p = pre_head
        while p:
            if p.next and p.next.val in nums:
                temp = p.next
                p.next = p.next.next
                temp.next = None
            else:
                p = p.next

        return pre_head.next


def test_modified_list():
    solution = Solution()
    assert solution.modifiedList([1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(
        5)))))).val == 4, 'wrong result'
    assert solution.modifiedList([1], ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(
        1)))))).val == 2, 'wrong result'


if __name__ == '__main__':
    test_modified_list()
