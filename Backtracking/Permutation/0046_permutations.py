from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(i, s):
            if i == n:
                res.append(path.copy())
                return

            for x in s:
                path.append(x)
                dfs(i + 1, s - {x})
                path.pop()

        dfs(0, set(nums))
        return res


def test_permute():
    solution = Solution()
    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
                                           [3, 2, 1]], 'wrong result'
    assert solution.permute([0, 1]) == [[0, 1], [1, 0]], 'wrong result'
    assert solution.permute([1]) == [[1]], 'wrong result'


if __name__ == '__main__':
    test_permute()
