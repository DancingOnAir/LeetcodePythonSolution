from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return len(nums) if len(nums) < 3 else (1 << len(nums).bit_length())


def test_unique_xor_triplets():
    solution = Solution()
    assert solution.uniqueXorTriplets([1, 2]) == 2, 'wrong result'
    assert solution.uniqueXorTriplets([3, 1, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_unique_xor_triplets()
