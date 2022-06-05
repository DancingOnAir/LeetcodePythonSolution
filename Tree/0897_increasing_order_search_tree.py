# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    # iterative + inorder
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        pre_head = TreeNode(float('inf'))
        cur = pre_head
        stk = [(root, False)]

        while stk:
            node, done = stk.pop()
            if done:
                cur.right = TreeNode(node.val)
                cur.left = None
                cur = cur.right
            else:
                if node.right:
                    stk.append((node.right, False))
                stk.append((node, True))
                if node.left:
                    stk.append((node.left, False))
        return pre_head.right

    # recursive + inorder
    def increasingBST1(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            if not self.res:
                self.res = TreeNode(root.val)
                self.cur = self.res
            else:
                self.cur.right = TreeNode(root.val)
                self.cur = self.cur.right

            inorder(root.right)

        self.res = None
        self.cur = None
        inorder(root)
        return self.res


def test_increasing_bst():
    solution = Solution()
    root = TreeNode(5, TreeNode(1), TreeNode(7))
    assert solution.increasingBST(root).val == 1, 'wrong result'
    assert solution.increasingBST(root).right.val == 5, 'wrong result'
    assert solution.increasingBST(root).right.right.val == 7, 'wrong result'


if __name__ == '__main__':
    test_increasing_bst()

