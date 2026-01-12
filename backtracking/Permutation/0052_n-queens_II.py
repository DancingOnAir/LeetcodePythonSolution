class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        on_path = [False] * n
        m = 2 * n - 1
        diag1 = [False] * m
        diag2 = [False] * m

        def dfs(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if not on_path[c] and not diag1[r + c] and not diag2[r - c]:
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False
        dfs(0)
        return res


def test_total_n_queens():
    solution = Solution()
    assert solution.totalNQueens(4) == 2, 'wrong result'
    assert solution.totalNQueens(1) == 1, 'wrong result'


if __name__ == '__main__':
    test_total_n_queens()
