from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(node, cur):
            cur.append(str(node.val))
            if not node.left and not node.right:
                self.res += int(''.join(cur), 2)
                return
            if node.left:
                preorder(node.left, cur)
                cur.pop()
            if node.right:
                preorder(node.right, cur)
                cur.pop()

        self.res = 0
        preorder(root, [])
        return self.res


def test_sum_root_to_leaf():
    solution = Solution()
    assert solution.sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))) == 22, 'wrong result'
    assert solution.sumRootToLeaf(TreeNode(0, TreeNode(1, TreeNode(0)), TreeNode(0, TreeNode(0, None, TreeNode(1, None, TreeNode(1))), TreeNode(0)))) == 5, 'wrong result'


if __name__ == '__main__':
    test_sum_root_to_leaf()

