from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        pass


def test_smallest_from_leaf():
    solution = Solution()
    assert solution.smallestFromLeaf(TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))) == 'dba', 'wrong result'
    assert solution.smallestFromLeaf(TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))) == 'adz', 'wrong result'
    assert solution.smallestFromLeaf(TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode(0))), TreeNode(1, TreeNode(0)))) == 'abc', 'wrong result'


if __name__ == '__main__':
    test_smallest_from_leaf()
