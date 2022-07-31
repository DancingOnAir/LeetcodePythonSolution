from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return max(left, right) + 1

        res = 0
        dfs(root)
        return res


def test_diameter_of_binary_tree():
    solution = Solution()
    assert solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3, 'wrong result'
    assert solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1, 'wrong result'


if __name__ == '__main__':
    test_diameter_of_binary_tree()


