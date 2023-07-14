from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test_middle_node():
    def print_link_list(head):
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res

    solution = Solution()
    assert print_link_list(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) == [3, 4, 5], 'wrong result'
    assert print_link_list(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))) == [4, 5, 6], 'wrong result'


if __name__ == '__main__':
    test_middle_node()
