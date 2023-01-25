from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def helper(mask, i):
            if i >= n:
                return 0
            if dp[mask] != -1:
                return dp[mask]

            res = 0
            for j in range(n):
                # 如果导师没有选中，那么可以尝试
                if (mask & (1 << j)) > 0:
                    cur = 0
                    for k in range(m):
                        cur += (students[i][k] == mentors[j][k])
                    res = max(res, cur + helper(mask ^ (1 << j), i + 1))
            dp[mask] = res
            return res

        n = len(students)
        m = len(students[0])
        dp = [-1] * (1 << n)
        return helper((1 << n) - 1, 0)


def test_max_compatibility_sum():
    solution = Solution()
    assert solution.maxCompatibilitySum([[1, 1, 0], [1, 0, 1], [0, 0, 1]],
                                        [[1, 0, 0], [0, 0, 1], [1, 1, 0]]) == 8, 'wrong result'
    assert solution.maxCompatibilitySum([[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_compatibility_sum()
