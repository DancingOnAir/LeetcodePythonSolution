from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(list)
        self.min_l, self.max_l = float('inf'), float('-inf')

        def dfs(root, x, y):
            self.min_l = min(self.min_l, x)
            self.max_l = max(self.max_l, x)
            m[x].append((y, root.val))
            if root.left:
                dfs(root.left, x - 1, y + 1)
            if root.right:
                dfs(root.right, x + 1, y + 1)

        dfs(root, 0, 0)
        res = list()
        for i in range(self.min_l, self.max_l + 1):
            res += [[j for i, j in sorted(m[i])]]
        return res

    def verticalTraversal1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stk = [(root, 0, 0)]
        q = list()
        while stk:
            node, r, c = stk.pop()
            q.append((node.val, r, c))

            if node.left:
                stk.append((node.left, r + 1, c - 1))
            if node.right:
                stk.append((node.right, r + 1, c + 1))
        q.sort(key=lambda x: (x[2], x[1], x[0]))

        res = list()
        i = float('inf')
        cur = list()
        for v, r, c in q:
            if i == c:
                cur.append(v)
            else:
                i = c
                if cur:
                    res.append(cur)
                cur = [v]

        if cur:
            res.append(cur)
        return res


def test_vertical_traversal():
    solution = Solution()
    assert solution.verticalTraversal(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[9],[3,15],[20],[7]], 'wrong result'
    assert solution.verticalTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))) == [[4],[2],[1,5,6],[3],[7]], 'wrong result'
    assert solution.verticalTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))) == [[4],[2],[1,5,6],[3],[7]], 'wrong result'


if __name__ == '__main__':
    test_vertical_traversal()
