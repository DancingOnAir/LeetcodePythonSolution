from typing import List
# from itertools import pairwise


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1]) % 2 == 0:
                return False
        return True

    # def isArraySpecial1(self, nums: List[int]) -> bool:
    #     return all(((x & 1) ^ (y & 1)) for x, y in pairwise(nums))


def test_is_array_special():
    solution = Solution()
    assert solution.isArraySpecial([1]), 'wrong result'
    assert solution.isArraySpecial([2, 1, 4]), 'wrong result'
    assert not solution.isArraySpecial([4, 3, 1, 6]), 'wrong result'


if __name__ == '__main__':
    test_is_array_special()
