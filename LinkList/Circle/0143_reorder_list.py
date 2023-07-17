from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def middle_of_linked_list(head):
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_linked_list(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre

                pre = cur
                cur = nxt
            return pre

        mid = middle_of_linked_list(head)
        head2 = reverse_linked_list(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt

            head = nxt
            head2 = nxt2


def test_reorder_list():
    def print_link_list(head):
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution.reorderList(head)
    assert print_link_list(head) == [1, 4, 2, 3], 'wrong result'

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution.reorderList(head)
    assert print_link_list(head) == [1, 5, 2, 4, 3], 'wrong result'


if __name__ == '__main__':
    test_reorder_list()
