from typing import Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(pa):
            if not pa:
                return 0
            l = dfs(pa.left)
            r = dfs(pa.right)

            nonlocal res
            res = max(res, l + r)
            return max(l, r) + 1

        res = 0
        dfs(root)
        return res

    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1

            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal res
            res = max(res, l + r + 2)

            return max(l, r) + 1

        res = 0
        dfs(root)
        return res


def test_diameter_of_binary_tree():
    solution = Solution()
    assert solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3, 'wrong result'


if __name__ == '__main__':
    test_diameter_of_binary_tree()
