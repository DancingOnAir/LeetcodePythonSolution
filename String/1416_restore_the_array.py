class Solution:
    # https://leetcode.com/problems/restore-the-array/discuss/585673/Python-rolling-DP
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n, mod = len(str(k)) + 1, len(s), 10 ** 9 + 7
        def valid(s):
            return s[0] != '0' and int(s) <= k

        dp = [0] * m
        for i in range(n-1, -1, -1):
            dp[i % m] = i > n - m and valid(s[i:])
            dp[i % m] = (dp[i % m] + sum(dp[j % m] for j in range(i+1, min(n, i+m)) if valid(s[i: j]))) % mod
        return dp[0]

    # O(len(k) * s)
    def numberOfArrays1(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(str(k)), len(s)
        #dp[i] 表示前i个数字进行恢复的方案数
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            num, base = 0, 1
            j = i - 1
            while j >= 0 and i - j <= m:
                num += (ord(s[j]) - 48) * base
                if num > k:
                    break
                if s[j] != '0':
                    dp[i] += dp[j]
                base *= 10
                j -= 1

            dp[i] %= MOD
        return dp[n]


def test_number_of_arrays():
    solution = Solution()

    assert solution.numberOfArrays("1000", 1000) == 1, 'wrong result'
    assert solution.numberOfArrays("1000", 10) == 0, 'wrong result'
    assert solution.numberOfArrays("1317", 2000) == 8, 'wrong result'
    assert solution.numberOfArrays("2020", 30) == 1, 'wrong result'
    assert solution.numberOfArrays("1234567890", 90) == 34, 'wrong result'


if __name__ == '__main__':
    test_number_of_arrays()
