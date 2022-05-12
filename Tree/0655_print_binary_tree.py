from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(root: Optional[TreeNode]):
            if root is None:
                return 0
            left_height = get_height(root.left)
            right_height = get_height(root.right)
            return max(left_height, right_height) + 1

        def helper(node, r, c):
            if node:
                res[r][c] = str(node.val)

                if node.left:
                    helper(node.left, r + 1, c - 2 ** (m - r - 2))
                if node.right:
                    helper(node.right, r + 1, c + 2 ** (m - r - 2))

        m = get_height(root)
        n = 2 ** m - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        helper(root, 0, (n - 1)//2)

        return res


def test_print_tree():
    solution = Solution()
    root = TreeNode(1, TreeNode(2))
    assert solution.printTree(root) == [["", "1", ""], ["2", "", ""]], 'wrong result'


if __name__ == '__main__':
    test_print_tree()

