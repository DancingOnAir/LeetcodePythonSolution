from typing import Optional, List
from bisect import bisect_left


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # in-order traverse
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(node, v):
            if node:
                dfs(node.left, v)
                v.append(node.val)
                dfs(node.right, v)

        nums = list()
        dfs(root, nums)
        res, n = list(), len(nums)
        for q in queries:
            i = bisect_left(nums, q)
            if i < n and nums[i] == q:
                res.append([q, q])
            else:
                if i == 0:
                    res.append([-1, nums[0]])
                elif i == n:
                    res.append([nums[-1], -1])
                else:
                    res.append([nums[i - 1], nums[i]])
        return res

    # TLE
    def closestNodes1(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        n = len(queries)
        res = [[-1, -1] for _ in range(n)]

        def dfs(node, i):
            if not node:
                return

            if node.val == queries[i]:
                res[i] = [node.val, node.val]
            elif node.val > queries[i]:
                if res[i][1] == -1 or node.val < res[i][1]:
                    res[i][1] = node.val
                dfs(node.left, i)
            else:
                if node.val > res[i][0]:
                    res[i][0] = node.val
                dfs(node.right, i)
            return

        for i in range(n):
            dfs(root, i)
        return res


def test_closest_nodes():
    solution = Solution()
    assert solution.closestNodes(TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(13, TreeNode(9), TreeNode(15, TreeNode(14)))), [2,5,16]) == [[2,2],[4,6],[15,-1]], 'wrong result'
    assert solution.closestNodes(TreeNode(4, None, TreeNode(9)), [3]) == [[-1,4]], 'wrong result'


if __name__ == '__main__':
    test_closest_nodes()
