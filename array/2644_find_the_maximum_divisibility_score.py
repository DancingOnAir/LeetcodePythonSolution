from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res, mx = 10 ** 9, 0
        for d in divisors:
            score = sum(x % d == 0 for x in nums)
            if mx < score:
                mx = score
                res = d
            elif mx == score:
                res = min(res, d)
        return res


def test_max_div_score():
    solution = Solution()
    assert solution.maxDivScore([2, 9, 15, 50], [5, 3, 7, 2]) == 2, 'wrong result'
    assert solution.maxDivScore([4, 7, 9, 3, 9], [5, 2, 3]) == 3, 'wrong result'
    assert solution.maxDivScore([20, 14, 21, 10], [10, 16, 20]) == 10, 'wrong result'


if __name__ == '__main__':
    test_max_div_score()
