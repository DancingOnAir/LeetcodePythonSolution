from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def preorder(node, pre, depth, val):
            if not node:
                return pre, -1

            if node.val == val:
                return pre, depth
            left = preorder(node.left, node, depth + 1, val)
            right = preorder(node.right, node, depth + 1, val)

            return left if left[1] >= 0 else right

        # return preorder(root, None, 0, x) == preorder(root, None, 0, y)
        rx = preorder(root, None, 0, x)
        ry = preorder(root, None, 0, y)
        return rx[1] == ry[1] and rx[0] != ry[0]


def test_is_cousins():
    solution = Solution()
    assert not solution.isCousins(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 4, 3), 'wrong result'
    assert solution.isCousins(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5))), 5, 4), 'wrong result'
    assert not solution.isCousins(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), 2, 3), 'wrong result'


if __name__ == '__main__':
    test_is_cousins()
