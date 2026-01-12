from typing import List
from itertools import permutations
from functools import lru_cache


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @lru_cache(None)
        def connect(w1, w2):
            return [w2[i:] for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]

        n = len(words)
        # dp[i][j] means dp[mask][last] will keep length of built string and built string itself.
        dp = [[(float('inf'), "")] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = (len(words[i]), words[i])

        for mask in range(1 << n):
            n_z_bits = [j for j in range(n) if mask & (1 << j)]

            for j, k in permutations(n_z_bits, 2):
                cand = dp[mask ^ (1 << j)][k][1] + connect(words[k], words[j])
                dp[mask][j] = min(dp[mask][j], (len(cand), cand))

        return min(dp[(1 << n) - 1])[1]


def test_shortest_superstring():
    solution = Solution()

    # assert solution.shortestSuperstring(["alex", "loves", "leetcode"]) == 'alexlovesleetcode'
    assert solution.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]) == 'gctaagttcatgcatc'


if __name__ == '__main__':
    test_shortest_superstring()
