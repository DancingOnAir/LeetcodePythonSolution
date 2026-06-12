from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(stk, node):
            while node:
                stk.append(node)
                node = node.left

        stk1, stk2 = list(), list()
        helper(stk1, root1)
        helper(stk2, root2)

        res = list()
        while stk1 or stk2:
            if not stk2:
                stk = stk1
            elif not stk1:
                stk = stk2
            else:
                stk = stk1 if stk1[-1].val < stk2[-1].val else stk2

            node = stk.pop()
            res.append(node.val)
            helper(stk, node.right)
        return res

    # inorder + sort
    def getAllElements1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = list()

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root1)
        inorder(root2)
        return sorted(res)


def test_get_all_elements():
    solution = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    assert solution.getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_get_all_elements()
