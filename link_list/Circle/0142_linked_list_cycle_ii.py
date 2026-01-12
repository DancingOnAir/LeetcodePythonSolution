from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None


def test_detect_cycle():
    solution = Solution()
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    head.next.next.next.next = head.next
    assert solution.detectCycle(head) is head.next, 'wrong result'

    head = ListNode(1)
    assert solution.detectCycle(head) is None, 'wrong result'


if __name__ == '__main__':
    test_detect_cycle()
