from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: Optional[TreeNode], cloned: Optional[TreeNode], target: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, target):
            if not node:
                return None
            if node.val == target:
                return node

            left = dfs(node.left, target)
            right = dfs(node.right, target)
            return left if left else right
        return dfs(cloned, target.val)

    def getTargetCopy1(self, original: Optional[TreeNode], cloned: Optional[TreeNode], target: Optional[TreeNode]) -> Optional[TreeNode]:
        if not original:
            return None
        if original == target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)


def test_get_target_copy():
    solution = Solution()
    original1 = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
    cloned1 = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
    target1 = original1.right
    res1 = cloned1.right
    assert solution.getTargetCopy(original1, cloned1, target1) == res1, 'wrong result'


if __name__ == '__main__':
    test_get_target_copy()
