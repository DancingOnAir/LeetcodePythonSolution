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


if __name__ == '__main__':
    test_largest_number()
