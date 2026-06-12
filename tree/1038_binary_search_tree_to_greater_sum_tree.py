from itertools import accumulate


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            node, stk, pre_sum = root, list(), 0
            while node or stk:
                while node:
                    stk.append(node)
                    node = node.right

                node = stk.pop()
                node.val = pre_sum = pre_sum + node.val
                node = node.left
        return root

    def bstToGst2(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)

        self.val += root.val
        root.val = self.val

        if root.left:
            self.bstToGst(root.left)
        return root

    def bstToGst1(self, root: TreeNode) -> TreeNode:
        vals = list()
        node = root
        stk = list()

        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            vals.append(node.val)
            node = node.right

        vals = list(accumulate(vals[::-1]))

        stk = list()
        node = root
        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            node.val = vals.pop()
            node = node.right
        return root


def test_bst_to_gst():
    solution = Solution()

    root1 = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    root2 = solution.bstToGst(root1)
    assert root2.val == 30, 'wrong result'
    assert root2.left.val == 36, 'wrong result'
    assert root2.right.val == 21, 'wrong result'

    root3 = TreeNode(0, None, TreeNode(1))
    root4 = solution.bstToGst(root3)
    assert root4.val == 1, 'wrong result'
    assert root4.right.val == 1, 'wrong result'


if __name__ == '__main__':
    test_bst_to_gst()
