from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        union = set(nums1) & set(nums2)
        if union:
            return sorted(union)[0]
        mi1, mi2 = min(nums1), min(nums2)
        return min(mi1 * 10 + mi2, mi2 * 10 + mi1)


def test_min_number():
    solution = Solution()
    assert solution.minNumber([4, 1, 3], nums2=[5, 7]) == 15, 'wrong result'
    assert solution.minNumber([3, 5, 2, 6], nums2=[3, 1, 7]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_number()
