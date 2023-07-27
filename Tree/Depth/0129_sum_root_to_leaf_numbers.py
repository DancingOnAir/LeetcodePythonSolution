from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return
            total = total * 10 + node.val
            if not node.left and not node.right:
                nonlocal res
                res += total
                return
            dfs(node.left, total)
            dfs(node.right, total)

        res = 0
        dfs(root, 0)
        return res


def test_sum_numbers():
    solution = Solution()
    assert solution.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25, 'wrong result'
    assert solution.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))) == 1026, 'wrong result'


if __name__ == '__main__':
    test_sum_numbers()
