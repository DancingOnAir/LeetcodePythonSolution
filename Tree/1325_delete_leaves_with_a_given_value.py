from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postorder(node):
            if not node:
                return True

            left = postorder(node.left)
            right = postorder(node.right)

            if left:
                node.left = None
            if right:
                node.right = None

            return left and right and node.val == target

        dummy = TreeNode(-1, root)
        postorder(dummy)
        return dummy.left


def test_remove_leaf_nodes():
    solution = Solution()

    root1 = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
    res1 = solution.removeLeafNodes(root1, 2)
    assert res1.val == 1, 'wrong result'
    assert not res1.left, 'wrong result'
    assert res1.right.val == 3, 'wrong result'
    assert not res1.right.left, 'wrong result'
    assert res1.right.right.val == 4, 'wrong result'

    root2 = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
    res2 = solution.removeLeafNodes(root2, 3)
    assert res2.val == 1, 'wrong result'
    assert res2.left.val == 3, 'wrong result'
    assert not res2.right, 'wrong result'
    assert not res2.left.left, 'wrong result'
    assert res2.left.right.val == 2, 'wrong result'

    root3 = TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2))))
    res3 = solution.removeLeafNodes(root3, 2)
    assert res3.val == 1, 'wrong result'
    assert not res3.left, 'wrong result'
    assert not res3.right, 'wrong result'


if __name__ == '__main__':
    test_remove_leaf_nodes()
