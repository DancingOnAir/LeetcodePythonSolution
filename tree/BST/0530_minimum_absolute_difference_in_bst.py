from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre = -1
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if self.pre != -1:
                nonlocal res
                res = min(res, abs(node.val - self.pre))
            self.pre = node.val
            dfs(node.right)

        res = float('inf')
        dfs(root)
        return res


def test_get_minimum_difference():
    solution = Solution()
    # assert solution.getMinimumDifference(TreeNode(1, None, TreeNode(2))) == 1, 'wrong result'
    assert solution.getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))) == 1, 'wrong result'
    assert solution.getMinimumDifference(TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))) == 1, 'wrong result'


if __name__ == '__main__':
    test_get_minimum_difference()
