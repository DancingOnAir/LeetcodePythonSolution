from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle_of_linked_list(head):
            slow = fast = head
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

        while head != mid:
            if head.val != head2.val:
                return False

            head = head.next
            head2 = head2.next
        return True


def test_is_palindrome():
    solution = Solution()
    assert solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))), 'wrong result'
    assert not solution.isPalindrome(ListNode(1, ListNode(2))), 'wrong result'


if __name__ == '__main__':
    test_is_palindrome()
