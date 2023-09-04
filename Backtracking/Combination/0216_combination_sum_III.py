from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, tot):
            d = k - len(path)
            if i < 0 or tot < 0 or (i + i - d + 1) * d // 2 < tot:
                return

            if len(path) == k:
                res.append(path.copy())
                return

            dfs(i - 1, tot)

            path.append(i)
            dfs(i - 1, tot - i)
            path.pop()

        dfs(9, n)
        return res

    # mode 2
    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, tot):
            d = k - len(path)
            if tot < 0 or tot > (i * 2 - d + 1) * d // 2:
                return

            if len(path) == k:
                res.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, tot - j)
                path.pop()

        dfs(9, n)
        return res


def test_combination_sum3():
    solution = Solution()
    assert solution.combinationSum3(3, 7) == [[4, 2, 1]], 'wrong result'
    # assert solution.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]], 'wrong result'
    assert solution.combinationSum3(4, 1) == [], 'wrong result'


if __name__ == '__main__':
    test_combination_sum3()
