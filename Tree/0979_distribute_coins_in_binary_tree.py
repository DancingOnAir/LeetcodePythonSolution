from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def distributeCoins(self, root: Optional[TreeNode], pre: Optional[TreeNode] = None) -> int:
        if not root:
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre:
            pre.val += root.val - 1
        return res + abs(root.val - 1)

    # dfs
    def distributeCoins1(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if not root:
                return 0

            left = postorder(root.left)
            right = postorder(root.right)

            self.res += abs(left) + abs(right)

            return root.val - 1 + left + right

        self.res = 0
        postorder(root)
        return self.res


def test_distribute_coins():
    solution = Solution()

    assert solution.distributeCoins(TreeNode(3, TreeNode(0), TreeNode(0))) == 2, 'wrong result'
    assert solution.distributeCoins(TreeNode(0, TreeNode(3), TreeNode(0))) == 3, 'wrong result'


if __name__ == '__main__':
    test_distribute_coins()
