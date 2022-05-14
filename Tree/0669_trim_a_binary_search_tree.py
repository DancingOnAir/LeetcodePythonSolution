from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def preorder(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if node:
                if parent is None:
                    if node.val < low:
                        return preorder(node.right, None)
                    elif node.val > high:
                        return preorder(node.left, None)
                else:
                    if node.val < low and parent:
                        parent.left = node.right
                        return preorder(node.right, parent)
                    elif node.val > high and parent:
                        parent.right = node.left
                        return preorder(node.left, parent)

                node.left = preorder(node.left, node)
                node.right = preorder(node.right, node)
                return node

            return None

        return preorder(root, None)


def test_trim_bst():
    solution = Solution()
    root = TreeNode(1, TreeNode(0), TreeNode(2))
    assert solution.trimBST(root, 1, 2).val == 1, 'wrong result'
    assert solution.trimBST(root, 1, 2).left is None, 'wrong result'
    assert solution.trimBST(root, 1, 2).right.val == 2, 'wrong result'

    root = TreeNode(1, None, TreeNode(2))
    assert solution.trimBST(root, 2, 4).val == 2, 'wrong result'
    assert solution.trimBST(root, 2, 4).left is None, 'wrong result'
    assert solution.trimBST(root, 2, 4).right is None, 'wrong result'


if __name__ == '__main__':
    test_trim_bst()
