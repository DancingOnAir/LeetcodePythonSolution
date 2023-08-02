from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def preorder_traversal(root):
    res = list()
    if not root:
        return res

    stk = [root]
    while stk:
        node = stk.pop()
        res.append(node.val)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)

    return res


def test_invert_tree():
    solution = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert preorder_traversal(solution.invertTree(root)) == [4, 7, 9, 6, 2, 3, 1], 'wrong result'
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert preorder_traversal(solution.invertTree(root)) == [2, 3, 1], 'wrong result'


if __name__ == '__main__':
    test_invert_tree()
