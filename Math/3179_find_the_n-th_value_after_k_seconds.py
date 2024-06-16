from math import comb


class Solution:
    # 二次项系数
    # https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/solutions/5282015/python-3-1-line-pascal-s-triangle-t-s-99-97/
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return comb(n + k - 1, n - 1) % (10 ** 9 + 7)

    # simulation
    def valueAfterKSeconds1(self, n: int, k: int) -> int:
        ps = [1] * n
        while k:
            for i in range(n - 1):
                ps[i + 1] += ps[i]
            k -= 1
        return ps[-1]


def test_value_after_k_seconds():
    solution = Solution()
    assert solution.valueAfterKSeconds(4, 5) == 56, 'wrong result'
    assert solution.valueAfterKSeconds(5, 3) == 35, 'wrong result'


if __name__ == '__main__':
    test_value_after_k_seconds()
