class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 1
        cnt1 = cnt2 = 0
        while startValue < target:
            startValue <<= 1
            cnt1 += 1
        if startValue == target:
            return cnt1
        r = startValue - target
        for i in range(cnt1, -1, -1):
            t = pow(2, i)
            coeff, r = divmod(r, t)
            cnt2 += coeff
            if r == 0:
                break
        return cnt1 + cnt2

    def brokenCalc1(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target & 1:
                target += 1
            else:
                target //= 2
        return res + startValue - target


def test_broken_calc():
    solution = Solution()
    assert solution.brokenCalc(2, 3) == 2, 'wrong result'
    assert solution.brokenCalc(5, 8) == 2, 'wrong result'
    assert solution.brokenCalc(3, 10) == 3, 'wrong result'


if __name__ == '__main__':
    test_broken_calc()
