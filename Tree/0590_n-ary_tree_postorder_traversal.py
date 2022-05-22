from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stk1 = [root]
        stk2 = []

        while stk1:
            node = stk1.pop()
            stk2.append(node)
            stk1.extend(node.children)

        res = list()
        while stk2:
            res.append(stk2.pop().val)
        return res

    def postorder1(self, root: 'Node') -> List[int]:
        self.res = list()

        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            self.res.append(root.val)

        dfs(root)
        return self.res


def test_postorder():
    solution = Solution()
    node3 = Node(3, [Node(5), Node(6)])
    root = Node(1, [node3, Node(2), Node(4)])
    assert solution.postorder(root) == [5, 6, 3, 2, 4, 1], 'wrong result'


if __name__ == '__main__':
    test_postorder()

