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
            return 0 if root is None else max(get_height(root.left), get_height(root.right)) + 1

        def update_value(node: Optional[TreeNode], lo, hi, depth):
            if node:
                mid = (lo + hi) // 2
                res[depth][mid] = str(node.val)
                update_value(node.left, lo, mid, depth + 1)
                update_value(node.right, mid + 1, hi, depth + 1)

        depth = get_height(root)
        res = [[""] * (2 ** depth - 1) for _ in range(depth)]
        update_value(root, 0, 2 ** depth - 1, 0)
        return res

    def printTree1(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(root: Optional[TreeNode]):
            return 0 if root is None else max(get_height(root.left), get_height(root.right)) + 1

        def helper(node, r, c):
            if node:
                res[r][c] = str(node.val)

                if node.left:
                    helper(node.left, r + 1, c - 2 ** (m - r - 2))
                if node.right:
                    helper(node.right, r + 1, c + 2 ** (m - r - 2))

        m = get_height(root)
        n = 2 ** m - 1
        res = [[""] * n for _ in range(m)]
        helper(root, 0, (n - 1)//2)

        return res


def test_print_tree():
    solution = Solution()
    root = TreeNode(1, TreeNode(2))
    assert solution.printTree(root) == [["", "1", ""], ["2", "", ""]], 'wrong result'


if __name__ == '__main__':
    test_print_tree()

