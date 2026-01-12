from typing import List
from functools import reduce
from operator import xor


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        xor_n2 = reduce(xor, nums)
        xor_n = reduce(xor, range(len(nums) - 2))

        xor_ab = xor_n2 ^ xor_n
        bit_diff = xor_ab & (-xor_ab)

        xor_n2_bit = reduce(xor, (x for x in nums if (x & bit_diff)))
        xor_n2_no_bit = reduce(xor, (x for x in nums if not (x & bit_diff)))

        xor_n_bit = reduce(xor, (x for x in range(len(nums) - 2) if (x & bit_diff)))
        xor_n_no_bit = reduce(xor, (x for x in range(len(nums) - 2) if not (x & bit_diff)))

        return [xor_n_no_bit ^ xor_n2_no_bit, xor_n_bit ^ xor_n2_bit]

    def getSneakyNumbers1(self, nums: List[int]) -> List[int]:
        m = [0] * (len(nums) - 2)
        res = []
        for x in nums:
            m[x] += 1
            if m[x] == 2:
                res.append(x)
        return res


def test_get_sneaky_numbers():
    solution = Solution()
    assert sorted(solution.getSneakyNumbers([0, 1, 1, 0])) == [0, 1], 'wrong result'
    assert sorted(solution.getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3], 'wrong result'
    assert solution.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]) == [4, 5], 'wrong result'


if __name__ == '__main__':
    test_get_sneaky_numbers()
