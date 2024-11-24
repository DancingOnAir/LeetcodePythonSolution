from itertools import accumulate


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if k > n:
            return 0
        elif k == n:
            return 1

        MOD = 10 ** 9 + 7
        res = 1
        cnt = 0
        cnts = []
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt - 1)
                    res = res * cnt % MOD
                k -= 1
                cnt = 0
        if k <= 0:
            return res

        # dp[i + 1][j]表示从前i种物品种选恰好j个物品的方案数
        # dp[0][0] = 1 表示什么都不选算一种方案
        dp = [[0] * k for _ in range(len(cnts) + 1)]
        dp[0][0] = 1
        for i, c in enumerate(cnts):
            ps = list(accumulate(dp[i], initial=0))
            for j in range(k):
                dp[i + 1][j] = (ps[j + 1] - ps[max(0, j - c)]) % MOD

        return (res - sum(dp[-1])) % MOD


def test_possible_string_count():
    solution = Solution()
    assert solution.possibleStringCount("aabbccdd", 7) == 5, 'wrong result'
    assert solution.possibleStringCount("aabbccdd", 8) == 1, 'wrong result'
    assert solution.possibleStringCount("aaabbb", 3) == 8, 'wrong result'


if __name__ == '__main__':
    test_possible_string_count()
