from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def postorder(root: Optional[TreeNode], leaf: List[int]):
            if not root:
                return

            postorder(root.left, leaf)
            postorder(root.right, leaf)
            if not root.left and not root.right:
                leaf.append(root.val)

        leaf1, leaf2 = list(), list()
        postorder(root1, leaf1)
        postorder(root2, leaf2)
        return leaf1 == leaf2


def test_leaf_similar():
    solution = Solution()
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(3), TreeNode(2))
    assert not solution.leafSimilar(root1, root2), 'wrong result'


if __name__ == '__main__':
    test_leaf_similar()
