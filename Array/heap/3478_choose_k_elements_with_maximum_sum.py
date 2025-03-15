from typing import List
from heapq import heappop, heappush


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        num_to_max = {}
        hp = []
        tot = 0
        for x, y in sorted(zip(nums1, nums2)):
            if x not in num_to_max:
                num_to_max[x] = tot
            tot += y
            heappush(hp, y)
            if len(hp) > k:
                tot -= heappop(hp)
        return [num_to_max[x] for x in nums1]

    # TLE
    def findMaxSum1(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0] * len(nums1)
        sorted_nums1 = sorted((x, i) for i, x in enumerate(nums1))
        for i, x in enumerate(nums1):
            hp = []
            for y, j in sorted_nums1:
                if x > y:
                    heappush(hp, -nums2[j])
            j = 0
            while hp and j < k:
                res[i] += -heappop(hp)
                j += 1
        return res


def test_find_max_sum():
    solution = Solution()
    assert solution.findMaxSum([4, 2, 1, 5, 3], nums2=[10, 20, 30, 40, 50], k=2) == [80, 30, 0, 80, 50], 'wrong result'
    assert solution.findMaxSum([2, 2, 2, 2], nums2=[3, 1, 2, 3], k=1) == [0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_find_max_sum()
