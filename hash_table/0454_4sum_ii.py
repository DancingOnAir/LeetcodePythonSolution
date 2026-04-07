from collections import defaultdict, Counter


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                ab[a + b] += 1

        res = 0
        for c in nums3:
            for d in nums4:
                res += ab[-c - d]
        return res

    # TLE
    def fourSumCount1(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        cnt3 = Counter(nums3)
        cnt4 = Counter(nums4)
        res = 0

        for k1, v1 in cnt1.items():
            for k2, v2 in cnt2.items():
                for k3, v3 in cnt3.items():
                    res += cnt4[-k1 - k2 - k3] * v1 * v2 * v3
        return res


def test_four_sum_count():
    solution = Solution()
    assert solution.fourSumCount([1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2, 'wrong result'
    assert solution.fourSumCount([0], nums2=[0], nums3=[0], nums4=[0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_four_sum_count()
