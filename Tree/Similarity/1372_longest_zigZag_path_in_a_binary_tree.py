from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        pass


def test_longest_zigzag():
    solution = Solution()
    assert solution.longestZigZag(TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))) == 3, 'wrong result'
    assert solution.longestZigZag(TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))) == 4, 'wrong result'
    assert solution.longestZigZag(TreeNode(1)) == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_zigzag()
