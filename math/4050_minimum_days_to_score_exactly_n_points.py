MX = 100_001
dp = [float('inf')] * MX
dp[0] = -1

tot = i = 1
while tot < MX:
    for j in range(tot, MX):
        dp[j] = min(dp[j], dp[j - tot] + i + 1)
    i += 1
    tot += i

class Solution:
    def minDays(self, n: int) -> int:
        return dp[n]

def test_min_days():
    solution = Solution()
    assert solution.minDays(2) == 3, 'wrong result'
    assert solution.minDays(9) == 6, 'wrong result'
    assert solution.minDays(12) == 7, 'wrong result'


if __name__ == '__main__':
    test_min_days()
