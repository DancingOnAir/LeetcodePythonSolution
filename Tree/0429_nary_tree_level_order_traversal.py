from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        dq = deque([root])
        res = list()
        while dq:
            sz = len(dq)
            tmp = list()
            while sz:
                x = dq.popleft()
                tmp.append(x.val)
                if x.children:
                    dq.extend(x.children)
                sz -= 1
            res.append(tmp)

        return res


def test_level_order():
    solution = Solution()
    node3 = Node(3, [Node(5), Node(6)])
    root = Node(1, [node3, Node(2), Node(4)])
    assert solution.levelOrder(root) == [[1], [3, 2, 4], [5, 6]], 'wrong result'


if __name__ == '__main__':
    test_level_order()
