from typing import Optional
import re

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", traversal)][::-1]

        def helper(depth):
            if not vals or vals[-1][0] != depth:
                return None

            root = TreeNode(vals.pop()[1])
            root.left = helper(depth + 1)
            root.right = helper(depth + 1)
            return root

        return helper(0)


def test_recover_from_preorder():
    solution = Solution()
    root1 = solution.recoverFromPreorder("1-2--3--4-5--6--7")
    assert root1.val == 1, 'wrong result'
    assert root1.left.val == 2, 'wrong result'
    assert root1.right.val == 5, 'wrong result'
    assert root1.left.left.val == 3, 'wrong result'
    assert root1.left.right.val == 4, 'wrong result'

    root2 = solution.recoverFromPreorder("1-2--3---4-5--6---7")
    assert root2.val == 1, 'wrong result'
    assert root2.left.val == 2, 'wrong result'
    assert root2.right.val == 5, 'wrong result'
    assert root2.left.left.val == 3, 'wrong result'
    assert root2.right.left.val == 6, 'wrong result'
    assert root2.left.left.left.val == 4, 'wrong result'
    assert root2.right.left.left.val == 7, 'wrong result'


if __name__ == '__main__':
    test_recover_from_preorder()
