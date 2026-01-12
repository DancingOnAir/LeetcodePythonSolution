from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = [0] * n
        m = 2 * n - 1
        on_path = [False] * n
        diag1 = [False] * m
        diag2 = [False] * m

        def dfs(r):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - 1 - c) for c in cols])
                return
            for c in range(n):
                if not on_path[c] and not diag1[r + c] and not diag2[r - c]:
                    cols[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False
        dfs(0)
        return res

    # pythonic
    def solveNQueens2(self, n: int) -> List[List[str]]:
        res = []
        cols = [0] * n

        def dfs(r, s):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - 1 - c) for c in cols])
                return

            for c in s:
                if all(r + c != R + cols[R] and r - c != R - cols[R] for R in range(r)):
                    cols[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return res

    # normal
    def solveNQueens1(self, n: int) -> List[List[str]]:
        res = []
        cols = [0] * n

        def valid(r, c):
            for R in range(r):
                C = cols[R]
                if R + C == r + c or R - C == r - c:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - 1 - c) for c in cols])
                return

            for c in s:
                if valid(r, c):
                    cols[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return res


def test_solve_n_queens():
    solution = Solution()
    assert solution.solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."],
                                        ["..Q.", "Q...", "...Q", ".Q.."]], 'wrong result'
    assert solution.solveNQueens(1) == [["Q"]], 'wrong result'


if __name__ == '__main__':
    test_solve_n_queens()
