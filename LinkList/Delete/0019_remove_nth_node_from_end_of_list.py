from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


def test_remove_nth_from_end():
    solution = Solution()
    assert solution.removeNthFromEnd(ListNode(1), 1) is None, 'wrong result'


if __name__ == '__main__':
    test_remove_nth_from_end()
