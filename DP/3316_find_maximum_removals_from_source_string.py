from typing import List
from functools import lru_cache


class Solution:
    # https://leetcode.cn/problems/find-maximum-removals-from-source-string/solutions/2948631/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-h94l/
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        targetIndices = set(targetIndices)

        @lru_cache(None)
        def dfs(i, j):
            if i < j:
                return float('-inf')
            if i < 0:
                return 0
            # 不选 source[i]，问题变成要使 pattern[0] 到 pattern[j] 是 source[0] 到 source[i−1] 的子序列，
            # 最多可以进行多少次删除操作，即 dfs(i−1,j)。如果 i 在 targetIndices 中，那么删除次数加一。
            res = dfs(i - 1, j) + (i in targetIndices)
            if j >= 0 and source[i] == pattern[j]:
                res = max(res, dfs(i - 1, j - 1))
            return res

        ans = dfs(len(source) - 1, len(pattern) - 1)
        return ans


def test_max_removals():
    solution = Solution()
    assert solution.maxRemovals("abbaa", "aba", [0, 1, 2]) == 1, 'wrong result'
    assert solution.maxRemovals("bcda", "d", [0, 3]) == 2, 'wrong result'
    assert solution.maxRemovals("dda", "dda", [0, 1, 2]) == 0, 'wrong result'
    assert solution.maxRemovals("yeyeykyded", "yeyyd", [0, 2, 3, 4]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_removals()
