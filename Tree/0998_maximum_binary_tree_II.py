from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pre, cur = None, root
        while cur and cur.val > val:
            pre, cur = cur, cur.right
        node = TreeNode(val)
        node.left = cur
        if pre:
            pre.right = node

        return root if root.val > val else node

    # if val is the largest, i = B.length-1, the root node's value is val, i=0 to i-1 are in the left child of root.
    # This explains why when val > root.val, root should be the left child of new node with value val.
    # Else val is not the largest, the new node with value val is always the right child of root.
    # recursive
    def insertIntoMaxTree2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree1(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node

    # inorder recursive
    def insertIntoMaxTree1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a = list()

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            a.append(node)
            inorder(node.right)

        inorder(root)
        for node in a[::-1]:
            if node.val > val:
                tmp = node.right
                node.right = TreeNode(val, tmp)
                return root

        return TreeNode(val, root)


def test_insert_into_max_tree():
    solution = Solution()
    assert solution.insertIntoMaxTree(TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2))), 5).val == 5, 'wrong result'
    assert solution.insertIntoMaxTree(TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4)), 3).val == 5, 'wrong result'
    assert solution.insertIntoMaxTree(TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4)), 3).right.right.val == 3, 'wrong result'
    assert solution.insertIntoMaxTree(TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(3)), 4).val == 5, 'wrong result'
    assert solution.insertIntoMaxTree(TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(3)), 4).right.val == 4, 'wrong result'


if __name__ == '__main__':
    test_insert_into_max_tree()

