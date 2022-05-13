from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = [(1, root)]
        while queue:
            res = max(res, queue[-1][0] - queue[0][0] + 1)
            # enumerate(iterable, start=0)
            # eg. s1 = "geek", list(enumerate(s1, 2))
            # result: [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
            queue = [child
                     for idx, node in queue
                     for child in enumerate((node.left, node.right), 2 * idx)
                     if child[1]]

        return res

    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        queue = [(root, 1)]

        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            temp = list()
            for node, i in queue:
                if node.left:
                    temp.append((node.left, 2 * i))
                if node.right:
                    temp.append((node.right, 2 * i + 1))
            queue = temp
        return res


def test_width_of_binary_tree():
    solution = Solution()
    node3 = TreeNode(3, TreeNode(5))
    root = TreeNode(1, node3, TreeNode(2))
    assert solution.widthOfBinaryTree(root) == 2, 'wrong result'


if __name__ == '__main__':
    test_width_of_binary_tree()
