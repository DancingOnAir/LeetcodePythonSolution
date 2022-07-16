# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def bfs(node, mx_ancestor):
            if node:
                if node.val >= mx_ancestor:
                    self.res += 1
                bfs(node.left, max(node.val, mx_ancestor))
                bfs(node.right, max(node.val, mx_ancestor))

        self.res = 0
        bfs(root, float('-inf'))
        return self.res


def test_good_nodes():
    solution = Solution()

    root1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert solution.goodNodes(root1) == 4, 'wrong result'

    root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    assert solution.goodNodes(root2) == 3, 'wrong result'


if __name__ == '__main__':
    test_good_nodes()

