from typing import Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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