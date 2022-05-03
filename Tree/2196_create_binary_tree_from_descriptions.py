from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        memo = dict()
        parents = set()

        for x, y, z in descriptions:
            if x not in memo:
                memo[x] = TreeNode(x)
                parents.add(x)
            if y not in memo:
                memo[y] = TreeNode(y)
            if y in parents:
                parents.remove(y)

            if z:
                memo[x].left = memo[y]
            else:
                memo[x].right = memo[y]

        for p in parents:
            return memo[p]


def level_order_traverse(root: Optional[TreeNode]):
    if not root:
        return []
    dq = deque()
    dq.append(root)

    res = list()
    while len(dq) > 0:
        x = dq.popleft()
        res.append(x.val)
        if x.left:
            dq.append(x.left)
        if x.right:
            dq.append(x.right)

    return res


def test_create_binary_tree():
    solution = Solution()
    root = solution.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
    assert level_order_traverse(root) == [50, 20, 80, 15, 17, 19], 'wrong result'
    root = solution.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
    assert level_order_traverse(root) == [1, 2, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_create_binary_tree()
