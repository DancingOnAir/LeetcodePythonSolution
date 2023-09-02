from typing import List


class Solution:
    # 模板1，选或者不选
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if len(path) == k:
                res.append(path.copy())
                return

            if i <= 0 or i < k - len(path):
                return

            dfs(i - 1)

            path.append(i)
            dfs(i - 1)
            path.pop()

        dfs(n)
        return res

    # 模板2
    def combine1(self, n: int, k: int) -> List[List[int]]:
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
