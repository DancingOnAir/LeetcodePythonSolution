from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            nonlocal res
            res = max(res, l + r + node.val)
            return max(l, r) + node.val

        res = 0
        dfs(root)
        return res


def test_max_path_sum():
    solution = Solution()
    assert solution.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6, 'wrong result'
    assert solution.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 42, 'wrong result'


if __name__ == '__main__':
    test_max_path_sum()
