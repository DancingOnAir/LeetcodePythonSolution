class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
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
