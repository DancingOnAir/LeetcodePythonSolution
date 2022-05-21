from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stk = [root]
        res = list()
        while stk:
            x = stk.pop()
            res.append(x.val)
            stk.extend(x.children[::-1])
        return res


def test_preorder():
    solution = Solution()
    node3 = Node(3, [Node(5), Node(6)])
    root = Node(1, [node3, Node(2), Node(4)])
    assert solution.preorder(root) == [1, 3, 5, 6, 2, 4], 'wrong result'


if __name__ == '__main__':
    test_preorder()

