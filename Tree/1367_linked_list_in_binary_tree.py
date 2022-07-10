from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        pass


def test_is_sub_path():
    solution = Solution()

    root1 = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
    head1 = ListNode(4, ListNode(2, ListNode(8)))
    assert solution.isSubPath(head1, root1), 'wrong result'

    root2 = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
    head2 = ListNode(1, ListNode(4, ListNode(2, ListNode(6))))
    assert solution.isSubPath(head2, root2), 'wrong result'

    root3 = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
    head3 = ListNode(1, ListNode(4, ListNode(2, ListNode(6, ListNode(8)))))
    assert not solution.isSubPath(head3, root3), 'wrong result'


if __name__ == '__main__':
    test_is_sub_path()
