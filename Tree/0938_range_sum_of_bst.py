from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return self.rangeSumBST(root.left, low, high) + root.val + self.rangeSumBST(root.right, low, high)


def test_range_sum_bst():
    solution = Solution()
    node5 = TreeNode(5, TreeNode(3), TreeNode(7))
    node15 = TreeNode(15, None, TreeNode(18))
    root = TreeNode(10, node5, node15)

    assert solution.rangeSumBST(root, 7, 15) == 32, 'wrong result'


if __name__ == '__main__':
    test_range_sum_bst()

