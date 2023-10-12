from functools import lru_cache


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        if s1.count('1') % 2 != s2.count('1') % 2:
            return -1

        @lru_cache(None)
        def dfs(i, free, pre_rev):
            if i < 0:
                return float('inf') if free > 0 or pre_rev else 0

            if (s1[i] == s2[i]) == (not pre_rev):
                return dfs(i - 1, free, False)
            res = min(dfs(i - 1, free + 1, False) + x, dfs(i - 1, free, True) + 1)

            if free:
                res = min(res, dfs(i - 1, free - 1, False))
            return res

        return dfs(len(s1) - 1, 0, False)


def test_min_operations():
    solution = Solution()
    # 1100011000
    # 0101001010
    # 0..3.5..8.
    assert solution.minOperations("1100011000", "0101001010", 2) == 4, 'wrong result'
    assert solution.minOperations("10110", "00011", 4) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
