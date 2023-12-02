class Solution:
    # dp[i][j] 表示把前面j个字符分割成i段
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        def is_prime(x):
            return x in {'2', '3', '5', '7'}

        def can_partition(j):
            return j == 0 or j == n or (not is_prime(s[j - 1]) and is_prime(s[j]))

        n, mod = len(s), 10 ** 9 + 7
        if k * minLength > n or not is_prime(s[0]) or is_prime(s[-1]):
            return 0

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        # 这里表示把空字符串0分割算1种
        dp[0][0] = 1
        for i in range(1, k + 1):
            total = 0
            # 给前后字符串预留出足够的长度
            for j in range(i * minLength, n - (k - i) * minLength + 1):
                if can_partition(j - minLength):
                    total = (total + dp[i - 1][j - minLength]) % mod
                if can_partition(j):
                    dp[i][j] = total
        return dp[k][n]


def test_beautiful_partitions():
    solution = Solution()
    assert solution.beautifulPartitions("23542185131", 3, 2) == 3, 'wrong result'
    assert solution.beautifulPartitions("23542185131", 3, 3) == 1, 'wrong result'
    assert solution.beautifulPartitions("3312958", 3, 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_beautiful_partitions()
