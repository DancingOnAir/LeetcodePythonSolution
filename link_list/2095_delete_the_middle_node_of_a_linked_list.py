from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        if n == 1:
            return None

        cur = head
        for i in range(n):
            if i == n // 2 - 1:
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = None
                del nxt
                break
            cur = cur.next
        return head


def test_delete_middle():
    solution = Solution()
    assert solution.deleteMiddle(ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))).val == 1, 'wrong result'
    assert solution.deleteMiddle(ListNode(2, ListNode(1))).next is None, 'wrong result'


if __name__ == '__main__':
    test_delete_middle()
