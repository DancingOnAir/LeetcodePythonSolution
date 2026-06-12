from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], level: int) -> bool:
            if not node:
                return True
            if level & 1:
                if node.val & 1:
                    return False
            else:
                if not (node.val & 1):
                    return False

            if level in m:
                if level & 1:
                    if m[level] <= node.val:
                        return False
                else:
                    if m[level] >= node.val:
                        return False
            m[level] = node.val
            return dfs(node.left, level + 1) and dfs(node.right, level + 1)

        m = dict()
        return dfs(root, 0)

    # level order
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        dq = deque([root])
        while len(dq) > 0:
            cur_level_size = len(dq)
            pre = float('inf') if level & 1 else 0

            while cur_level_size > 0:
                x = dq.popleft()
                if level & 1:
                    if x.val & 1 or pre <= x.val:
                        return False
                else:
                    if not (x.val & 1) or pre >= x.val:
                        return False

                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
                pre = x.val
                cur_level_size -= 1
            level += 1
        return True


def test_is_even_odd_tree():
    solution = Solution()

    node3 = TreeNode(3, TreeNode(12), TreeNode(8))
    node7 = TreeNode(7, TreeNode(6))
    node9 = TreeNode(9, None, TreeNode(2))
    node10 = TreeNode(10, node3)
    node4 = TreeNode(4, node7, node9)
    root = TreeNode(1, node10, node4)
    assert solution.isEvenOddTree(root), 'wrong result'


if __name__ == "__main__":
    test_is_even_odd_tree()

