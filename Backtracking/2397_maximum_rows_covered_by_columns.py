from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        def dfs(i):
            nonlocal cnt
            if cnt == numSelect:
                cur = 0
                for r in matrix:
                    if all(select[j] == 1 for j, c in enumerate(r) if c == 1):
                        cur += 1

                nonlocal res
                res = max(res, cur)

            if i >= n:
                return

            dfs(i + 1)

            select[i] += 1
            cnt += 1
            dfs(i + 1)

            select[i] -= 1
            cnt -= 1

        m, n = len(matrix), len(matrix[0])
        res = cnt = 0
        select = [0] * n
        dfs(0)
        return res


def test_maximum_rows():
    solution = Solution()
    assert solution.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2) == 3, 'wrong result'
    assert solution.maximumRows([[1], [0]], 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_rows()
