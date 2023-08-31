from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            d = k - len(path)
            # if i < d:
            #     return

            if len(path) == k:
                res.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return res


def test_combine():
    solution = Solution()
    assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], 'wrong result'
    assert solution.combine(1, 1) == [[1]], 'wrong result'


if __name__ == '__main__':
    test_combine()
