from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node:
                return 0
            total = postorder(node.left) + postorder(node.right) + node.val
            self.vals.append(total)
            return total

        self.vals = list()
        total = postorder(root)
        return max(v * (total - v) for v in self.vals) % (10 ** 9 + 7)

    def maxProduct1(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + node.val

        self.res = total = 0
        total = dfs(root)
        dfs(root)
        return self.res % (10 ** 9 + 7)


def test_max_product():
    solution = Solution()
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert solution.maxProduct(root1) == 110, 'wrong result'
    root2 = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
    assert solution.maxProduct(root2) == 90, 'wrong result'


if __name__ == '__main__':
    test_max_product()
