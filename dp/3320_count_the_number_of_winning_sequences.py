from functools import lru_cache
from math import pow


class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        m = {c: i for i, c in enumerate('FWE')}
        s = [m[c] for c in s]

        @lru_cache(None)
        def dfs(i, bal, ban):
            if -bal > i:
                return 0
            if bal > i + 1:
                return pow(2, i + 1) % MOD
            res = 0
            # 枚举召唤物FWE
            for k in range(3):
                if k == ban:
                    continue
                score = (k - s[i]) % 3
                if score == 2:
                    score = -1
                res += dfs(i - 1, bal + score, k)
            return res % MOD

        return dfs(len(s) - 1, 0, -1)


def test_count_winning_sequences():
    solution = Solution()
    assert solution.countWinningSequences("FFF") == 3, 'wrong result'
    assert solution.countWinningSequences("FWEFW") == 18, 'wrong result'


if __name__ == '__main__':
    test_count_winning_sequences()
