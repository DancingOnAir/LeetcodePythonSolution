from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, p, g):
            if not node:
                return

            if g and g.val % 2 == 0:
                self.res += node.val
            dfs(node.left, node, p)
            dfs(node.right, node, p)

        self.res = 0
        dfs(root, None, None)
        return self.res


def test_sum_event_grandparent():
    solution = Solution()
    root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    assert solution.sumEvenGrandparent(root) == 18, 'wrong'


if __name__ == '__main__':
    test_sum_event_grandparent()
