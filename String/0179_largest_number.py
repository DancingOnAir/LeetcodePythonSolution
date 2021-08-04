from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
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
