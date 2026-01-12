from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque([root, root])
        while dq:
            n1 = dq.popleft()
            n2 = dq.popleft()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            else:
                if n1.val != n2.val:
                    return False
                dq.append(n1.left)
                dq.append(n2.right)
                dq.append(n1.right)
                dq.append(n2.left)
        return True

    # recursive
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 and node2 and node1.val == node2.val:
                return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            return node1 == node2
        return not root or dfs(root.left, root.right)


def test_is_symmetric():
    solution = Solution()
    assert solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))), 'wrong result'
    assert not solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))), 'wrong result'


if __name__ == '__main__':
    test_is_symmetric()
