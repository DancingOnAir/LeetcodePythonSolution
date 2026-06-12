from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        root.val = 0
        while dq:
            n = len(dq)
            tot = 0
            tmp = []
            for _ in range(n):
                node = dq.popleft()
                tmp.append(node)
                if node.left:
                    dq.append(node.left)
                    tot += node.left.val
                if node.right:
                    dq.append(node.right)
                    tot += node.right.val

            for node in tmp:
                t = tot
                if node.left:
                    t -= node.left.val
                if node.right:
                    t -= node.right.val
                if node.left:
                    node.left.val = t
                if node.right:
                    node.right.val = t
        return root


def test_replace_value_in_tree():
    solution = Solution()
    root = TreeNode(3, TreeNode(1), TreeNode(2))
    assert solution.replaceValueInTree(root).val == 0, 'wrong result'
    assert solution.replaceValueInTree(root).left.val == 0, 'wrong result'
    assert solution.replaceValueInTree(root).right.val == 0, 'wrong result'


if __name__ == '__main__':
    test_replace_value_in_tree()
