from typing import List


class Solution:
    # 从添加元素思考
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2 = set(nums1), set(nums2)
        intersection_size = len(set1 & set2)
        n = len(nums1)
        l1 = min(n // 2, len(set1) - intersection_size)
        l2 = min(n // 2, len(set2) - intersection_size)
        # l1 + l2 + min(n - l1 - l2, intersection_size)
        return min(n, l1 + l2 + intersection_size)

    # 从移除元素思考
    def maximumSetSize1(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1) // 2
        set1, set2 = set(nums1), set(nums2)
        # 移除nums1中重复的元素:len(nums1) - len(set1)，那么之后还需要移除的元素个数为: m - (len(nums1) - len(set1))
        rm1 = max(0, len(set1) - m)
        rm2 = max(0, len(set2) - m)
        union_size = len(set1 | set2)
        intersection_size = len(set1 & set2)

        if rm1 > 0:
            rm = min(rm1, intersection_size)
            rm1 -= rm
            intersection_size -= rm
        if rm2 > 0:
            rm = min(rm2, intersection_size)
            rm2 -= rm

        return union_size - rm1 - rm2


def test_maximum_set_size():
    solution = Solution()
    assert solution.maximumSetSize([1, 2, 1, 2], [1, 1, 1, 1]) == 2, 'wrong result'
    assert solution.maximumSetSize([1, 2, 3, 4, 5, 6], [2, 3, 2, 3, 2, 3]) == 5, 'wrong result'
    assert solution.maximumSetSize([1, 1, 2, 2, 3, 3], [4, 4, 5, 5, 6, 6]) == 6, 'wrong result'


if __name__ == '__main__':
    test_maximum_set_size()
