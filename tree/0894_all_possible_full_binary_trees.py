from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1 == 0:
            return []

        self.res = defaultdict(list)
        self.res[1] = [TreeNode()]

        for i in range(3, n+1, 2):
            for j in range(1, n, 2):
                k = i - 1 - j
                for left in self.res[j]:
                    for right in self.res[k]:
                        self.res[i].append(TreeNode(0, left, right))
        return self.res[n]

    # dp
    def allPossibleFBT2(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode()]

        for i in range(3, n+1, 2):
            for j in range(1, n, 2):
                k = i - 1 - j
                for left in dp[j]:
                    for right in dp[k]:
                        root = TreeNode(0, left, right)
                        dp[i].append(root)
        return dp[n]

    # Complexity: Time O(N!), Space O(N!)
    def allPossibleFBT1(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1 == 0:
            return []
        if n == 1:
            return [TreeNode()]

        res = list()
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - 1 - i)

            for l in left:
                for r in right:
                    root = TreeNode()
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


def test_all_possible_fbt():
    solution = Solution()
    assert solution.allPossibleFBT(7)[0].val == 0, 'wrong result'


if __name__ == '__main__':
    test_all_possible_fbt()
