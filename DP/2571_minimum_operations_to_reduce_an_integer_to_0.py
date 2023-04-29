class Solution:
    # dfs
    def minOperations(self, n: int) -> int:
        def dfs(x):
            if x & (x - 1) == 0:
                return 1
            low_bit = x & -x
            return 1 + min(dfs(x + low_bit << 1), dfs(x - low_bit << 1))

        return dfs(n)

    # bit manipulation
    def minOperations1(self, n: int) -> int:
        res = 1
        while n & (n - 1):
            low_bit = n & -n
            # 多个连续1
            if n & (low_bit << 1):
                n += low_bit
            else:
                n -= low_bit
            res += 1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(39) == 3, 'wrong result'
    assert solution.minOperations(54) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
