from collections import defaultdict
from functools import lru_cache


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            res = float('inf')
            cnt = defaultdict(int)
            max_count = 0
            for j in range(i, n):
                cnt[s[j]] += 1
                if cnt[s[j]] > max_count:
                    max_count = cnt[s[j]]

                if j - i + 1 == len(cnt) * max_count:
                    res = min(res, dfs(j + 1) + 1)
            return res

        return dfs(0)


def test_minimum_substring_in_partition():
    solution = Solution()
    assert solution.minimumSubstringsInPartition("fabccddg") == 3, 'wrong result'
    assert solution.minimumSubstringsInPartition("abababaccddb") == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_substring_in_partition()

