class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [0] + [float('inf')] * sum
        for x in nums:
            for i in range(sum, 0, -1):
                a = 0
                while x >> a:
                    b = 0
                    while x >> a << b <= i:
                        dp[i] = min(dp[i], dp[i - (x >> a << b)] + a + b)
                        b += 1
                    a += 1

                    if dp[sum] == 0:
                        return 0
        return -1 if dp[sum] == float('inf') else dp[sum]


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([10, 2], sum=13) == 3, 'wrong result'
    assert solution.minOperations([6, 3], sum=8) == 2, 'wrong result'
    assert solution.minOperations([2, 2], sum=7) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
