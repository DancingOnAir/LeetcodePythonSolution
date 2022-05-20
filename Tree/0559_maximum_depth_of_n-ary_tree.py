from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
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
