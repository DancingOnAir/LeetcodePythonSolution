from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def test_delete_duplicate():
    def print_linked_list(head):
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_linked_list(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))) == [1, 2], 'wrong result'
    assert print_linked_list(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))) == [1, 2, 3], 'wrong result'


if __name__ == '__main__':
    test_delete_duplicate()
