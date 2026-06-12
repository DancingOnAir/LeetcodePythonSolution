from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # dfs返回的意义使当前节点是否被删除
        def postorder(node, total):
            if not node.left and not node.right:
                return node.val + total < limit

            left_deleted = True
            right_deleted = True
            if node.left:
                left_deleted = postorder(node.left, total + node.val)
            if node.right:
                right_deleted = postorder(node.right, total + node.val)
            if left_deleted:
                node.left = None
            if right_deleted:
                node.right = None

            return left_deleted and right_deleted

        root_deleted = postorder(root, 0)
        if root_deleted:
            return None
        return root


def test_sufficient_subset():
    solution = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(-5)), TreeNode(-3, TreeNode(4)))
    res = solution.sufficientSubset(root, -1)

    assert res.val == 1, 'wrong result'
    assert not res.left, 'wrong result'
    assert res.right.val == -3, 'wrong result'
    assert res.right.left.val == 4, 'wrong result'


if __name__ == '__main__':
    test_sufficient_subset()

