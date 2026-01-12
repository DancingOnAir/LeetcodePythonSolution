from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


def test_has_cycle():
    solution = Solution()
    head = ListNode(1)
    tail = ListNode(2)
    head.next = tail
    tail.next = head
    assert solution.hasCycle(head), 'wrong result'
    assert not solution.hasCycle(ListNode(1)), 'wrong result'


if __name__ == '__main__':
    test_has_cycle()
