# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            if not self.res:
                self.res = TreeNode(root.val)
                self.cur = self.res
            else:
                self.cur.right = TreeNode(root.val)
                self.cur = self.cur.right

            inorder(root.right)

        self.res = None
        self.cur = None
        inorder(root)
        return self.res


def test_increasing_bst():
    solution = Solution()
    root = TreeNode(5, TreeNode(1), TreeNode(7))
    assert solution.increasingBST(root).val == 1, 'wrong result'
    assert solution.increasingBST(root).right.val == 5, 'wrong result'
    assert solution.increasingBST(root).right.right.val == 7, 'wrong result'


if __name__ == '__main__':
    test_increasing_bst()

