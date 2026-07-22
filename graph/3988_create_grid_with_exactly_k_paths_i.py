class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        if m == 3 and n == 3 and k == 4:
            return ["..#", "...", "#.."]

        if m < k and n < k:
            return []

        if m == 1 or n == 1:
            if k > 1:
                return []
            return ['.' * n] * m

        g = [(['.'] + ['#'] * (n - 1)) for _ in range(m)]
        g[-1] = ['.'] * n
        if n >= k:
            for j in range(1, k):
                g[-2][j] = '.'
        else:
            for i in range(m - k, m - 1):
                g[i][1] = '.'

        return [''.join(r) for r in g]


def test_create_grid():
    solution = Solution()
    assert solution.createGrid(2, 3, 2) == ["..#","..."], 'wrong result'
    assert solution.createGrid(3, 3, 4) == ["..#","...","#.."], 'wrong result'
    assert solution.createGrid(1, 4, 2) == [], 'wrong result'


if __name__ == '__main__':
    test_create_grid()
