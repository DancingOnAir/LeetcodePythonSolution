from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # recursive
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        return 1 + max(map(self.maxDepth, root.children or [None]))

    # improved bfs
    def maxDepth2(self, root: 'Node') -> int:
        q = list()
        if root:
            q.append((root, 1))

        res = 0
        for node, level in q:
            res = level
            q += [(child, level + 1) for child in node.children if child]
        return res

    # bfs
    def maxDepth1(self, root: 'Node') -> int:
        if not root:
            return 0

        res = 0
        q = [root]

        while q:
            tmp = list()
            for node in q:
                if node.children:
                    for child in node.children:
                        tmp.append(child)
            q = tmp
            res += 1
        return res


def test_max_depth():
    solution = Solution()
    node3 = Node(3, [Node(5), Node(6)])
    root = Node(1, [node3, Node(2), Node(4)])
    assert solution.maxDepth(root) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_depth()
