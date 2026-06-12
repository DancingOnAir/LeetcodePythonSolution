from typing import Optional
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 【验证二叉搜索树【基础算法精讲 11】】 https://www.bilibili.com/video/BV14G411P7C1/?share_source=copy_web&vd_source=1fe6e1be7076869ed72407a8374a4eba
    # preorder
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        return left < root.val < right and self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)

    pre = float('-inf')

    # inorder
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
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
