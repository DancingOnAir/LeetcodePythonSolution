from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
