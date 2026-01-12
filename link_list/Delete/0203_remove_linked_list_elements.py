from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


def test_remove_elements():
    def print_linked_list(head):
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_linked_list(solution.removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6)) == [1, 2, 3, 4, 5], 'wrong result'
    assert print_linked_list(solution.removeElements(None, 1)) == [], 'wrong result'
    assert print_linked_list(solution.removeElements(ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7)) == [], 'wrong result'


if __name__ == '__main__':
    test_remove_elements()
