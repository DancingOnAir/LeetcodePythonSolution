from collections import Counter


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        for k, v in cnt1.items():
            if k in cnt2:
                cnt2[k] -= v
        res = 0
        for v in cnt2.values():
            if v & 1:
                return -1
            if v > 0:
                res += v
        return res // 2


def test_min_cost():
    solution = Solution()
    assert solution.minCost([1, 1, 1], nums2=[1, 2, 2]) == 1, 'wrong result'
    assert solution.minCost([10, 20], nums2=[20, 10]) == 0, 'wrong result'
    assert solution.minCost([10, 10], nums2=[20, 20]) == 1, 'wrong result'
    assert solution.minCost([10, 20], nums2=[30, 40]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
