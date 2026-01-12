from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def helper(x):
            r = int(x ** 0.5)
            if r * r == x:
                return 0

            cnt = 0
            res = 1 + x
            for i in range(2, r + 1):
                if x % i == 0:
                    res += i + x // i
                    cnt += 1
                if cnt == 2:
                    return 0
            return res if cnt == 1 else 0

        return sum(helper(x) for x in nums)


def test_sum_four_divisors():
    solution = Solution()
    assert solution.sumFourDivisors([21, 4, 7]) == 32, 'wrong result'
    assert solution.sumFourDivisors([21, 21]) == 64, 'wrong result'
    assert solution.sumFourDivisors([1, 2, 3, 4, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_sum_four_divisors()
