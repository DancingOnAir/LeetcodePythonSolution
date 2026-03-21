class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [1] + [0] * m
        for i, x in enumerate(s):
            for j in range(min(i, m - 1), max(m - n + i, 0) - 1, -1):
                if x == t[j]:
                    dp[j + 1] += dp[j]
        return dp[m]

    def maxInsertC(self, s: str) -> int:
        cnt_t = s.count('T')
        cnt_l = 0
        res = 0
        for c in s:
            if c == 'T':
                cnt_t -= 1
            if c == 'L':
                cnt_l += 1
            res = max(res, cnt_l * cnt_t)
        return res

    def numOfSubsequences(self, s: str) -> int:
        extra = max(self.numDistinct(s, 'CT'), self.numDistinct(s, 'LC'), self.maxInsertC(s))
        return self.numDistinct(s, 'LCT') + extra


def test_num_of_subsequences():
    solution = Solution()
    assert solution.numOfSubsequences("LMCT") == 2, 'wrong result'
    assert solution.numOfSubsequences("LCCT") == 4, 'wrong result'
    assert solution.numOfSubsequences("L") == 0, 'wrong result'


if __name__ == '__main__':
    test_num_of_subsequences()
