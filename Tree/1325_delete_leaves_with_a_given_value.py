from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        pass


def test_remove_leaf_nodes():
    solution = Solution()
    root1 = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
    res1 = solution.removeLeafNodes(root1, 2)
    assert res1.val == 1, 'wrong result'
    assert not res1.left, 'wrong result'
    assert res1.right.val == 3, 'wrong result'
    assert not res1.right.left, 'wrong result'
    assert not res1.right.right.val == 4, 'wrong result'


if __name__ == '__main__':
    test_remove_leaf_nodes()
