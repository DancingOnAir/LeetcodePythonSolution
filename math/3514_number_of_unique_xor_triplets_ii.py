from typing import List
from itertools import combinations


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = list(set(nums))
        st = {x ^ y for x, y in combinations(nums, 2)} | {0}
        return len({xy ^ z for xy in st for z in nums})


def test_unique_xor_triplets():
    solution = Solution()
    assert solution.uniqueXorTriplets([1, 3]) == 2, 'wrong result'
    assert solution.uniqueXorTriplets([6, 7, 8, 9]) == 4, 'wrong result'


if __name__ == '__main__':
    test_unique_xor_triplets()
