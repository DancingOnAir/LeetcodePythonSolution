from typing import Optional
from heapq import heappop, heappush


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def level_order(r):
            pass

        q = [root]
        stk = list()
        while q:
            cur = 0
            temp = list()
            for node in q:
                cur += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
            heappush(stk, cur)
            if len(stk) > k:
                heappop(stk)
        return heappop(stk) if len(stk) == k else -1


def test_kth_largest_level_sum():
    solution = Solution()
    assert solution.kthLargestLevelSum(TreeNode(5, TreeNode(8, TreeNode(2), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7))), 4) == -1, 'wrong result'
    assert solution.kthLargestLevelSum(TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7))), 2) == 13, 'wrong result'
    assert solution.kthLargestLevelSum(TreeNode(1, TreeNode(2, TreeNode(3))), 1) == 3, 'wrong result'


if __name__ == '__main__':
    test_kth_largest_level_sum()
