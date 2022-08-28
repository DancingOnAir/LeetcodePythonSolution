from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x + diff in nums and x + diff * 2 in nums:
                res += 1
        return res


def test_arithmetic_triplets():
    solution = Solution()
    assert solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2, 'wrong result'
    assert solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_arithmetic_triplets()
