from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # recursive return left, right, result
        # left is the maximum length in direction of root.left
        # right is the maximum length in direction of root.right
        # result is the maximum length in the whole subtree.
        def dfs(node):
            if not node:
                return -1, -1, -1
            left = dfs(node.left)
            right = dfs(node.right)
            return left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])

        return dfs(root)[2]


def test_longest_zigzag():
    solution = Solution()

    root1 = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
    assert solution.longestZigZag(root1) == 3, 'wrong result'

    root2 = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
    assert solution.longestZigZag(root2) == 4, 'wrong result'

    root3 = TreeNode(1)
    assert solution.longestZigZag(root3) == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_zigzag()
