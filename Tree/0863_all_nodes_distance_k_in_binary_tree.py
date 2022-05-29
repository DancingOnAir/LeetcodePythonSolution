from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent):
            if root and parent:
                graph[parent.val].add(root.val)
                graph[root.val].add(parent.val)
            # inorder traverse
            if root.left:
                dfs(root.left, root)
            if root.right:
                dfs(root.right, root)

        graph = defaultdict(set)
        dfs(root, None)

        res = [target.val]
        seen = set(res)
        for i in range(k):
            new_level = list()
            for cur_node_val in res:
                for next_node_val in graph[cur_node_val]:
                    if next_node_val not in seen:
                        new_level.append(next_node_val)

            res = new_level
            seen |= set(res)

        return res
        pass


def test_distance_k():
    solution = Solution()
    node2 = TreeNode(2, TreeNode(7), TreeNode(4))
    node5 = TreeNode(5, TreeNode(6), node2)
    node1 = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, node5, node1)
    assert sorted(solution.distanceK(root, TreeNode(5), 2)) == [1, 4, 7], 'wrong result'


if __name__ == '__main__':
    test_distance_k()
