from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for k in count:
            if count[k] == 1:
                return k

    def singleNumber1(self, nums: List[int]) -> int:
        x1, x2, mask = 0, 0, 0
        for num in nums:
            x2 ^= (x1 & num)
            x1 ^= num

            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask

        return x1


def test_single_number():
    solution = Solution()

    assert solution.singleNumber([2, 2, 3, 2]) == 3, "wrong result"
    assert solution.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99, "wrong result"


if __name__ == '__main__':
    test_single_number()
