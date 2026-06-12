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
        def get_path(root, target, path):
            if not root:
                return False
            if root.val == target.val:
                return True

            path.append(root)
            if get_path(root.left, target, path) or get_path(root.right, target, path):
                return True

            path.pop()
            return False

        def get_k_distance_nodes(root, k):
            if not root:
                return []
            if not k:
                return [root.val]
            return get_k_distance_nodes(root.left, k-1) + get_k_distance_nodes(root.right, k-1)

        if not k:
            return [target.val]
        path = list()
        if not get_path(root, target, path):
            return []

        res = get_k_distance_nodes(target, k)

        cur = target
        while path and k > 0:
            parent = path.pop()
            k -= 1

            if k == 0:
                res.append(parent.val)
            elif parent.left == cur:
                res += get_k_distance_nodes(parent.right, k-1)
            else:
                res += get_k_distance_nodes(parent.left, k-1)

            cur = parent
        return res

    # dfs + bfs
    def distanceK1(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
    assert sorted(solution.distanceK(root, node5, 2)) == [1, 4, 7], 'wrong result'


if __name__ == '__main__':
    test_distance_k()
