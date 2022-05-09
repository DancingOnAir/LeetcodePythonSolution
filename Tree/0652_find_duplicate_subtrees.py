from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def tuplify(root):
            if root:
                k = frozenset([(root.val, tuplify(root.left), tuplify(root.right))])
                trees[k].append(root)
                return k

        trees = defaultdict(list)
        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]

    def findDuplicateSubtrees1(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def tuplify(root):
            if root:
                # the type of k is tuple
                k = root.val, tuplify(root.left), tuplify(root.right)
                trees[k].append(root)
                return k
        trees = defaultdict(list)
        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]


def test_find_duplicate_substree():
    solution = Solution()

    root = TreeNode(2, TreeNode(1), TreeNode(1))
    assert solution.findDuplicateSubtrees(root) == TreeNode(1), 'wrong result'


if __name__ == '__main__':
    test_find_duplicate_substree()
