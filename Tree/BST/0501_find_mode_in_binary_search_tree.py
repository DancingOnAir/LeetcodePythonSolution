from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre_val, pre_cnt = float('-inf'), 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            if node.val == self.pre_val:
                self.pre_cnt += 1
            else:
                self.pre_cnt = 1
                self.pre_val = node.val

            nonlocal max_cnt, res
            if max_cnt == self.pre_cnt:
                res.append(self.pre_val)
            elif max_cnt < self.pre_cnt:
                max_cnt = self.pre_cnt
                res = [self.pre_val]

            dfs(node.right)

        res = list()
        max_cnt = 0
        dfs(root)
        return res


def test_find_mode():
    solution = Solution()
    assert solution.findMode(TreeNode(1, None, TreeNode(2, TreeNode(2)))) == [2], 'wrong result'
    assert solution.findMode(TreeNode(0)) == [0], 'wrong result'


if __name__ == '__main__':
    test_find_mode()
