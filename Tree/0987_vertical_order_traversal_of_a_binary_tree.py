from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
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
