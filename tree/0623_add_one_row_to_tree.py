from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root or depth <= 0:
            return None

        if depth == 1:
            return TreeNode(val, root)

        if depth == 2:
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

    def addOneRow1(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        dq = deque([root])
        while depth > 0:
            sz = len(dq)
            while sz > 0:
                x = dq.popleft()
                if depth == 2:
                    x.left = TreeNode(val, x.left, None)
                    x.right = TreeNode(val, None, x.right)
                else:
                    if x.left:
                        dq.append(x.left)
                    if x.right:
                        dq.append(x.right)
                sz -= 1

            depth -= 1
        return root


def inorder_traverse(root: Optional[TreeNode]) -> List[int]:
    res = list()
    stk = list()
    node = root

    while len(stk) > 0 or node:
        if node:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            res.append(node.val)
            node = node.right

    return res


def test_add_one_row():
    solution = Solution()

    node2 = TreeNode(2, TreeNode(3), TreeNode(1))
    node6 = TreeNode(6, TreeNode(5))
    root = TreeNode(4, node2, node6)
    assert inorder_traverse(solution.addOneRow(root, 1, 2)) == [3, 2, 1, 1, 4, 1, 5, 6], 'wrong result'


if __name__ == '__main__':
    test_add_one_row()
