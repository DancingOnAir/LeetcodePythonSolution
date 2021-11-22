from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list((set(nums1) & set(nums2)) | (set(nums1) & set(nums3)) | (set(nums2) & set(nums3)))


def test_two_out_of_three():
    solution = Solution()

    assert solution.twoOutOfThree([1, 1, 3, 2], [2, 3], [3]) == [3, 2], 'wrong result'
    assert solution.twoOutOfThree([3, 1], [2, 3], [1, 2]) == [2, 3, 1], 'wrong result'
    assert solution.twoOutOfThree([1, 2, 2], [4, 3, 3], [5]) == [], 'wrong result'


if __name__ == '__main__':
    test_two_out_of_three()
