from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            d = k - len(path)

            if len(path) == k:
                if sum(path) == n:
                    res.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(9)
        return res


def test_combination_sum3():
    solution = Solution()
    assert solution.combinationSum3(3, 7) == [[4, 2, 1]], 'wrong result'
    # assert solution.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]], 'wrong result'
    assert solution.combinationSum3(4, 1) == [], 'wrong result'


if __name__ == '__main__':
    test_combination_sum3()
