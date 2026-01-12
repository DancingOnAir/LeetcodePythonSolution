from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(grid):
            res += r[::-1] if i % 2 else r
        return res[::2]

    def zigzagTraversal1(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            if i & 1:
                res += grid[i][::-1][(n & 1)::2]
            else:
                res += grid[i][::2]
        return res


def test_zigzag_traversal():
    solution = Solution()
    assert solution.zigzagTraversal([[1, 2], [3, 4]]) == [1, 4], 'wrong result'
    assert solution.zigzagTraversal([[2, 1], [2, 1], [2, 1]]) == [2, 1, 2], 'wrong result'
    assert solution.zigzagTraversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 3, 5, 7, 9], 'wrong result'


if __name__ == '__main__':
    test_zigzag_traversal()
