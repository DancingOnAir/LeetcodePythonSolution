class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [0] + [float('inf')] * sum
        for x in nums:
            l = x.bit_length()
            for i in range(sum, 0, -1):
                a = 0
                while x << a <= i:
                    dp[i] = min(dp[i], dp[i - (x << a)] + a)
                    a += 1
                a = l - 1
                while a > 0 and x >> a <= i:
                    dp[i] = min(dp[i], dp[i - (x >> a)] + a)
                    a -= 1
        return -1 if dp[sum] == float('inf') else dp[sum]


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([5, 6, 10], sum=4) == 3, 'wrong result'
    assert solution.minOperations([10, 2], sum=13) == 3, 'wrong result'
    assert solution.minOperations([6, 3], sum=8) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
