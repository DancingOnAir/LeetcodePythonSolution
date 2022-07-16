# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # one line + recursive
    def goodNodes(self, root: TreeNode, mx=-100000) -> int:
        return (self.goodNodes(root.left, max(root.val, mx)) + self.goodNodes(root.right, max(root.val, mx)) + (root.val >= mx)) if root else 0

    def goodNodes1(self, root: TreeNode) -> int:
        def bfs(node, mx_ancestor):
            if node:
                if node.val >= mx_ancestor:
                    self.res += 1
                bfs(node.left, max(node.val, mx_ancestor))
                bfs(node.right, max(node.val, mx_ancestor))

        self.res = 0
        bfs(root, root.val)
        return self.res


def test_good_nodes():
    solution = Solution()

    root1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert solution.goodNodes(root1) == 4, 'wrong result'

    root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    assert solution.goodNodes(root2) == 3, 'wrong result'


if __name__ == '__main__':
    test_good_nodes()

