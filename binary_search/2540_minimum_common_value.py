from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1)

    def getCommon1(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1


def test_get_common():
    solution = Solution()
    assert solution.getCommon([1, 2, 3], [2, 4]) == 2, 'wrong result'
    assert solution.getCommon([1, 2, 3, 6], [2, 3, 4, 5]) == 2, 'wrong result'


if __name__ == '__main__':
    test_get_common()
