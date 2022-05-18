from typing import Optional, List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def isLeaf(self, grid):
        return all(grid[i][j] == grid[0][0]
                   for i in range(len(grid))
                   for j in range(len(grid)))

    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)
        return Node(grid[0][0],
                    False,
                    self.construct1([row[:n//2] for row in grid[:n//2]]),
                    self.construct1([row[n//2:] for row in grid[:n//2]]),
                    self.construct1([row[:n//2] for row in grid[n//2:]]),
                    self.construct1([row[n//2:] for row in grid[n//2:]]))

    def construct1(self, grid: List[List[int]]) -> 'Node':
        def is_same_value(x, y, l):
            for i in range(x, x + l):
                for j in range(y, y + l):
                    if grid[i][j] != grid[x][y]:
                        return False
            return True

        def helper(x, y, l):
            if l == 1 or is_same_value(x, y, l):
                return Node(grid[x][y], True, None, None, None, None)

            node = Node(grid[x][y], False, None, None, None, None)
            node.topLeft = helper(x, y, l // 2)
            node.topRight = helper(x, y + l // 2, l // 2)
            node.bottomLeft = helper(x + l // 2, y, l // 2)
            node.bottomRight = helper(x + l // 2, y + l // 2, l // 2)

            return node

        return helper(0, 0, len(grid))


def test_construct():
    solution = Solution()

    root = solution.construct([[0, 1], [1, 0]])
    assert not root.isLeaf and root.val == 0, 'wrong result'
    assert root.topLeft.isLeaf and root.topLeft.val == 0, 'wrong result'
    assert root.topRight.isLeaf and root.topRight.val == 1, 'wrong result'
    assert root.bottomLeft.isLeaf and root.bottomLeft.val == 1, 'wrong result'
    assert root.bottomRight.isLeaf and root.bottomRight.val == 0, 'wrong result'


if __name__ == '__main__':
    test_construct()
