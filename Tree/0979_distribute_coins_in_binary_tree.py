from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if not root:
                return 0

            left = postorder(root.left)
            right = postorder(root.right)

            root.val += left + right
            self.res += abs(root.val - 1)

            return root.val - 1

        self.res = 0
        postorder(root)
        return self.res


def test_distribute_coins():
    solution = Solution()

    assert solution.distributeCoins(TreeNode(3, TreeNode(0), TreeNode(0))) == 2, 'wrong result'
    assert solution.distributeCoins(TreeNode(0, TreeNode(3), TreeNode(0))) == 3, 'wrong result'


if __name__ == '__main__':
    test_distribute_coins()
