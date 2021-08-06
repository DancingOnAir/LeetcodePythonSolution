from typing import List
from functools import cmp_to_key


class Solution:
    # (a>b) - (a<b) 等价于 a<b时为-1, a=b时为0, a>b时为1
    # 这里x+y=a, y+x=b, 为了逆序排列参数 lambda y, x 而不是x, y.
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums), key=cmp_to_key(lambda y, x:  ((x+y) > (y+x)) - ((x+y) < (y+x)) ))).lstrip('0') or '0'

    def largestNumber1(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x + y < y + x:
                return -1
            else:
                return 1

        nums = sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True)
        return ''.join(nums).lstrip('0') or '0'


def test_largest_number():
    solution = Solution()

    assert solution.largestNumber([10, 2]) == '210', 'wrong result'
    assert solution.largestNumber([3, 30, 34, 5, 9]) == '9534330', 'wrong result'
    assert solution.largestNumber([1]) == '1', 'wrong result'
    assert solution.largestNumber([10]) == '10', 'wrong result'


def test_lambda_cmp():
    # 如果返回负数，说明x排在y前面
    # 如果返回正数，说明x排在y后面
    # 如果返回0，说明x和y无先后关系
    def cmp(y, x):
        if x < y:
            return -2
        elif x == y:
            return 0
        return 3

    nums = [3, 5, 2, 1, 4, 9, 6, 8, 7, 0]
    nums = sorted(nums, key=cmp_to_key(cmp))
    print(nums)


if __name__ == '__main__':
    # test_lambda_cmp()
    test_largest_number()
