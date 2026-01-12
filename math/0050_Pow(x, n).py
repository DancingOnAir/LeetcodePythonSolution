from math import isclose


class Solution:
    # recursive
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)

        if n & 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n >> 1)

    # iterative
    def myPow1(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)

        res = 1
        while n:
            if n & 0b1:
                res *= x
            x *= x
            n >>= 1
        return res


def test_my_pow():
    solution = Solution()
    assert isclose(solution.myPow(2.00000, 10), 1024.00000, rel_tol=1e-5), 'wrong result'
    assert isclose(solution.myPow(2.10000, 3), 9.26100, rel_tol=1e-5), 'wrong result'
    assert isclose(solution.myPow(2.00000, -2), 0.25000, rel_tol=1e-5), 'wrong result'


if __name__ == '__main__':
    test_my_pow()
