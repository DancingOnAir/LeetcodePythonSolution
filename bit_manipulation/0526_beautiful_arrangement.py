class Solution:
    # dp[mask]表示在选择mask里二进制为1的数时的方案数，比如mask=0110表示前2个数选择了数字2，3
    # dp[0] = 1表示不选择任何数也是一种方案
    def countArrangement(self, n: int) -> int:
        dp = [0] * (1 << n)
        dp[0] = 1
        for bitmask in range(1 << n):
            bits = bin(bitmask).count('1')
            for i in range(n):
                if bitmask & (1 << i) and ((i + 1) % bits == 0 or bits % (i + 1) == 0):
                    dp[bitmask] += dp[bitmask ^ (1 << i)]
        return dp[(1 << n) - 1]


def test_count_arrangement():
    solution = Solution()
    assert solution.countArrangement(2) == 2, 'wrong result'
    assert solution.countArrangement(1) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_arrangement()
