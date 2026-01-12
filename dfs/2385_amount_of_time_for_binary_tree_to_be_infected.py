from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def preorder(node, graph):
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                preorder(node.left, graph)
                preorder(node.right, graph)

        def dfs(u, pa, depth, graph):
            nonlocal res
            res = max(res, depth)

            for v in graph[u]:
                if v != pa:
                    dfs(v, u, depth + 1, graph)

        g = defaultdict(list)
        preorder(root, g)
        res = 0
        dfs(start, -1, 0, g)

        return res


def test_amount_of_time():
    solution = Solution()
    assert solution.amountOfTime(TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6))), 3) == 4, 'wrong result'
    assert solution.amountOfTime(TreeNode(1), 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_amount_of_time()
