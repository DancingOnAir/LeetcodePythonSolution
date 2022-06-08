from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not (root1 and root2):
            return False

        if root1.val == root2.val:
            if root1.left and root2.left and root1.right and root2.right:
                if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
                    return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                elif root1.left.val == root2.right.val and root1.right.val == root2.left.val:
                    return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
                else:
                    return False
            elif root1.left and root2.left and not root1.right and not root2.right:
                if root1.left.val == root2.left.val:
                    return self.flipEquiv(root1.left, root2.left)
                else:
                    return False
            elif root1.left and root2.right and not root1.right and not root2.left:
                if root1.left.val == root2.right.val:
                    return self.flipEquiv(root1.left, root2.right)
                else:
                    return False
            elif root1.right and root2.left and not root1.left and not root2.right:
                if root1.right.val == root2.left.val:
                    return self.flipEquiv(root1.right, root2.left)
                else:
                    return False
            elif root1.right and root2.right and not root1.left and not root2.left:
                if root1.right.val == root2.right.val:
                    return self.flipEquiv(root1.right, root2.right)
                else:
                    return False
            elif not (root1.left or root1.right or root2.left or root2.right):
                return True

            return False


def test_flip_equiv():
    solution = Solution()
    # node51 = TreeNode(5, TreeNode(7), TreeNode(8))
    # node21 = TreeNode(2, TreeNode(4), node51)
    # node31 = TreeNode(3, TreeNode(6))
    # root1 = TreeNode(1, node21, node31)
    #
    # node52 = TreeNode(5, TreeNode(8), TreeNode(7))
    # node32 = TreeNode(3, None, TreeNode(6))
    # node22 = TreeNode(2, TreeNode(4), node52)
    # root2 = TreeNode(1, node32, node22)
    # assert solution.flipEquiv(root1, root2), 'wrong result'

    assert not solution.flipEquiv(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2, TreeNode(3)))), 'wrong result'


if __name__ == '__main__':
    test_flip_equiv()
