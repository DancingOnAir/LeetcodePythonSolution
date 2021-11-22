from typing import List
from collections import Counter


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = Counter()
        for nums in nums1, nums2, nums3:
            c.update(set(nums))
        return [k for k, v in c.items() if v > 1]

    def twoOutOfThree1(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return (set(nums1) & set(nums2)) | (set(nums1) & set(nums3)) | (set(nums2) & set(nums3))


def test_two_out_of_three():
    solution = Solution()

    assert solution.twoOutOfThree([1, 1, 3, 2], [2, 3], [3]) == [3, 2], 'wrong result'
    assert solution.twoOutOfThree([3, 1], [2, 3], [1, 2]) == [2, 3, 1], 'wrong result'
    assert solution.twoOutOfThree([1, 2, 2], [4, 3, 3], [5]) == [], 'wrong result'


if __name__ == '__main__':
    test_two_out_of_three()
