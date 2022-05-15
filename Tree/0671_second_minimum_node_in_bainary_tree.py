from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node:
                if root.val < node.val < self.res:
                    self.res = node.val
                if node.val == root.val:
                    dfs(node.left)
                    dfs(node.right)

        self.res = float('inf')
        dfs(root)
        return self.res if self.res != float('inf') else -1

    def findSecondMinimumValue1(self, root: Optional[TreeNode]) -> int:
        res = -1
        dq = deque([root])

        while dq:
            x = dq.popleft()
            # 比res大的节点不需要进队列
            if x.left:
                if res == -1 or x.val < res:
                    dq.append(x.left)
            if x.right:
                if res == -1 or x.val < res:
                    dq.append(x.right)
            # root一定是最小值，x需要严格比root大
            if x.val > root.val:
                if res == -1 or x.val < res:
                    res = x.val

        return res


def test_find_second_minimum_value():
    solution = Solution()
    root = TreeNode(2, TreeNode(2), TreeNode(2))
    assert solution.findSecondMinimumValue(root) == -1, 'wrong result'


if __name__ == '__main__':
    test_find_second_minimum_value()
