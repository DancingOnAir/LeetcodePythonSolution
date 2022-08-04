from typing import Optional, List, Set
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        def inorder(val):
            # check cycle
            if val in seen:
                self.invalid = True
                return

            seen.add(val)
            node = nodes[val]
            if node.left:
                node.left = inorder(node.left.val)
            # check inorder increasing
            if val <= self.cur:
                self.invalid = True
                return

            self.cur = val
            if node.right:
                node.right = inorder(node.right.val)
            return node

        in_degree = defaultdict(int)
        nodes = dict()
        for root in trees:
            if root.val not in in_degree:
                in_degree[root.val] = 0

            if root.left:
                in_degree[root.left.val] += 1
                if root.left.val not in nodes:
                    nodes[root.left.val] = root.left

            if root.right:
                in_degree[root.right.val] += 1
                if root.right.val not in nodes:
                    nodes[root.right.val] = root.right
            # if leaf nodes of previous trees have the same value with this root, just replace it.
            nodes[root.val] = root

        sources = [k for k, v in in_degree.items() if v == 0]
        if len(sources) != 1:
            return None

        self.cur = float('-inf')
        self.invalid = False
        seen = set()
        res = inorder(sources[0])
        if len(seen) != len(nodes) or self.invalid:
            return None
        return res


def test_can_merge():
    solution = Solution()

    res1 = solution.canMerge([TreeNode(2, TreeNode(1)), TreeNode(3, TreeNode(2), TreeNode(5)), TreeNode(5, TreeNode(4))])
    assert res1.val == 3, 'wrong result'
    assert res1.left.val == 2, 'wrong result'
    assert res1.right.val == 5, 'wrong result'

    res2 = solution.canMerge([TreeNode(5, TreeNode(3), TreeNode(8)), TreeNode(3, TreeNode(2), TreeNode(6))])
    assert res2.val == 5, 'wrong result'
    assert res2.left.val == 3, 'wrong result'
    assert res2.right.val == 8, 'wrong result'

    res3 = solution.canMerge([TreeNode(5, TreeNode(4)), TreeNode(3)])
    assert not res3, 'wrong result'


if __name__ == '__main__':
    test_can_merge()
