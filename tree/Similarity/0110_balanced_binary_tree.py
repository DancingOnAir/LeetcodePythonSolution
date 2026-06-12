from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            left_max = depth(node.left)
            right_max = depth(node.right)
            if left_max == -1 or right_max == -1:
                return -1
            if abs(left_max - right_max) > 1:
                return -1
            return max(left_max, right_max) + 1
        return depth(root) != -1



def test_is_balanced():
    solution = Solution()
    assert solution.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), 'wrong result'
    assert not solution.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))), 'wrong result'


if __name__ == '__main__':
    test_is_balanced()
