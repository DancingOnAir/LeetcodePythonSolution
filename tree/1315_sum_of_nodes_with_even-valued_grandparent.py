from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bfs
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        dq = deque([(root, False)])
        while dq:
            parent, even_grandparent = dq.popleft()
            even_parent = (parent.val % 2 == 0)
            for child in (parent.left, parent.right):
                if child:
                    dq.append((child, even_parent))
                    res += child.val if even_grandparent else 0
        return res

    # dfs
    def sumEvenGrandparent1(self, root: TreeNode) -> int:
        def dfs(node, p, g):
            if not node:
                return

            if g and g.val % 2 == 0:
                self.res += node.val
            dfs(node.left, node, p)
            dfs(node.right, node, p)

        self.res = 0
        dfs(root, None, None)
        return self.res


def test_sum_event_grandparent():
    solution = Solution()
    root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    assert solution.sumEvenGrandparent(root) == 18, 'wrong'


if __name__ == '__main__':
    test_sum_event_grandparent()
