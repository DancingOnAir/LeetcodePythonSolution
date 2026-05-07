from collections import deque


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        res = [[0] * m for _ in range(n)]
        for x, y, c in sources:
            res[x][y] = c

        sources.sort(key=lambda x: -x[2])
        q = deque(sources)

        while q:
            i, j, c = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < m and res[x][y] == 0:
                    res[x][y] = c
                    q.append([x, y, c])
        return res


def test_color_grid():
    solution = Solution()
    assert solution.colorGrid(3, 3, [[0, 0, 1], [2, 2, 2]]) == [[1, 1, 2], [1, 2, 2], [2, 2, 2]], 'wrong result'
    assert solution.colorGrid(3, 3, [[0, 1, 3], [1, 1, 5]]) == [[3, 3, 3], [5, 5, 5], [5, 5, 5]], 'wrong result'
    assert solution.colorGrid(2, 2, [[1, 1, 5]]) == [[5, 5], [5, 5]], 'wrong result'


if __name__ == '__main__':
    test_color_grid()
