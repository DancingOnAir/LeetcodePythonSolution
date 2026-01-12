class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0

        n = len(num)
        res = 0
        mod = 10 ** 9 + 7

        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def helper(k, i, j):
            l = lcp[k][i]
            return l >= j + 1 - i or num[k + l] < num[i + l]

        for j in range(n):
            dp[0][j] = 1
        for i in range(1, n):
            if num[i] == '0':
                continue
            k = i - 1
            s = 0
            for j in range(i, n):
                dp[i][j] = s
                if k < 0:
                    continue
                if num[k] > '0' and helper(k, i, j):
                    dp[i][j] = (dp[i][j] + dp[k][i - 1]) % mod
                s = (s + dp[k][i - 1]) % mod
                k -= 1
        for i in range(n):
            res = (res + dp[i][n - 1]) % mod
        return res


def test_number_of_combinations():
    solution = Solution()
    assert solution.numberOfCombinations("327") == 2, 'wrong result'
    assert solution.numberOfCombinations("094") == 0, 'wrong result'
    assert solution.numberOfCombinations("0") == 0, 'wrong result'
    assert solution.numberOfCombinations("9999999999999") == 101, 'wrong result'


if __name__ == '__main__':
    test_number_of_combinations()
