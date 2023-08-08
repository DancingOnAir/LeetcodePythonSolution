from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre = float('-inf')

    # inorder
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val

        return self.isValidBST(root.right)


def test_is_valid_bst():
    solution = Solution()
    assert solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))), 'wrong result'
    assert not solution.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))), 'wrong result'


if __name__ == '__main__':
    test_is_valid_bst()
