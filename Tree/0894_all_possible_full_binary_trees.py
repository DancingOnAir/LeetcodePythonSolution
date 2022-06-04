from typing import List, Optional


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
