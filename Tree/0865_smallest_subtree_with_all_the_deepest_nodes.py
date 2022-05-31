from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #  Intuitively, we should be traversing from the children to the parent and calculate the
    #  height from bottom. So the null nodes would have height 0. The leaf nodes would have the
    #  height 1 and the root would have the max height.
    #
    #  At each node, we keep a pair<height_of_node_from_bottom, node>. At a given node, if we
    #  realize that the leftHeight == rightHeight, it means we have found the deepest subtree
    #  rooted at node. If leftHeight > rightHeight, it means the deepest subtree must be rooted
    #  at left child. If rightHeight > leftHeight, it means the deepest subtree must be rooted
    #  at right child.
    #
    #  Which traversal allows us to traverse from bottom-up? Postorder! So we use it in the code.
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deep(node: Optional[TreeNode]):
            if not node:
                return 0, None

            left = deep(node.left)
            right = deep(node.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif right[0] > left[0]:
                return right[0] + 1, right[1]
            else:
                return left[0] + 1, node
        return deep(root)[1]


def test_subtree_with_deepest():
    solution = Solution()

    node2 = TreeNode(2, TreeNode(7), TreeNode(4))
    node5 = TreeNode(5, TreeNode(6), node2)
    node1 = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, node5, node1)
    assert solution.subtreeWithAllDeepest(root) == node2, 'wrong result'


if __name__ == '__main__':
    test_subtree_with_deepest()
