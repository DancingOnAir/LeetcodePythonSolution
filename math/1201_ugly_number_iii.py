from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l1 = lcm(a, b)
        l2 = lcm(b, c)
        l3 = lcm(a, c)
        l4 = lcm(a, b, c)

        def cal(x):
            cnt = x // a + x // b + x // c - x // l1 - x // l2 - x // l3 + x // l4
            return cnt >= n

        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) >> 1
            if cal(mid):
                r = mid
            else:
                l = mid + 1
        return l


def test_nth_ugly_number():
    solution = Solution()
    assert solution.nthUglyNumber(3, 2, 3, 5) == 4, 'wrong result'
    assert solution.nthUglyNumber(4, 2, 3, 4) == 6, 'wrong result'
    assert solution.nthUglyNumber(5, 2, 11, 13) == 10, 'wrong result'


if __name__ == '__main__':
    test_nth_ugly_number()
