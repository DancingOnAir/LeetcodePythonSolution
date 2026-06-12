from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def traverse(node: Optional[TreeNode], val: int) -> int:
            if not node:
                return 0

            left = traverse(node.left, node.val)
            right = traverse(node.right, node.val)
            self.res = max(self.res, left + right)

            return 0 if val != node.val else 1 + max(left, right)

        self.res = 0
        traverse(root, -1)
        return self.res

    def longestUnivaluePath1(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            path_left = dfs(node.left)
            path_right = dfs(node.right)

            path_left = path_left + 1 if node.left and node.val == node.left.val else 0
            path_right = path_right + 1 if node.right and node.val == node.right.val else 0
            self.res = max(self.res, path_left + path_right)

            return max(path_left, path_right)

        dfs(root)
        return self.res


def test_longest_univalue_path():
    solution = Solution()

    node4 = TreeNode(4, TreeNode(4), TreeNode(4))
    node5 = TreeNode(5, None, TreeNode(5))
    root = TreeNode(1, node4, node5)
    assert solution.longestUnivaluePath(root) == 2, 'wrong result'

    node4 = TreeNode(4, TreeNode(1), TreeNode(1))
    node5 = TreeNode(5, None, TreeNode(5))
    root = TreeNode(5, node4, node5)
    assert solution.longestUnivaluePath(root) == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_univalue_path()
