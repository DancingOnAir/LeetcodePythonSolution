from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


def test_search_bst():
    solution = Solution()
    node2 = TreeNode(2, TreeNode(1), TreeNode(3))
    root = TreeNode(4, node2, TreeNode(7))
    assert solution.searchBST(root, 2).val == 2, 'wrong result'
    assert solution.searchBST(root, 2).left.val == 1, 'wrong result'
    assert solution.searchBST(root, 2).right.val == 3, 'wrong result'


if __name__ == '__main__':
    test_search_bst()
