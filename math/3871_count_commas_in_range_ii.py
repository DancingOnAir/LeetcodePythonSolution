class Solution:
    def countCommas(self, n: int) -> int:
        def helper(x):
            # 表示x位数拥有的q个逗号
            q = (x - 1) // 3
            # x位数一共有9 * 10 ** (x - 1)个
            return q * (9 * 10 ** (x - 1))

        m = len(str(n))
        if m < 4:
            return 0
        res = 0
        for i in range(4, m):
            res += helper(i)
        q = (m - 1) // 3
        res += (n - 10 ** (m - 1) + 1) * q
        return res

    def countCommas1(self, n: int) -> int:
        res = 0
        low = 1000
        while low <= n:
            res += n - low + 1
            low *= 1000
        return res


def test_count_commas():
    solution = Solution()
    assert solution.countCommas(100000) == 99001, 'wrong result'
    assert solution.countCommas(1002) == 3, 'wrong result'
    assert solution.countCommas(998) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_commas()
