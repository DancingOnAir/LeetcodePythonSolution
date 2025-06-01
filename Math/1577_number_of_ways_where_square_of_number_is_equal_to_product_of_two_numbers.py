from typing import List
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(arr):
            c1 = Counter()
            c2 = Counter()
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    if i == j:
                        c1[arr[i] * arr[j]] += 1
                    else:
                        c2[arr[i] * arr[j]] += 1
            return c1, c2

        s1, m1 = helper(nums1)
        s2, m2 = helper(nums2)
        res = 0
        for k, v in s1.items():
            if k in m2:
                res += v * m2[k]
        for k, v in s2.items():
            if k in m1:
                res += v * m1[k]
        return res


def test_num_triplets():
    solution = Solution()
    assert solution.numTriplets([7, 4], nums2=[5, 2, 8, 9]) == 1, 'wrong result'
    assert solution.numTriplets([1, 1], nums2=[1, 1, 1]) == 9, 'wrong result'
    assert solution.numTriplets([7, 7, 8, 3], nums2=[1, 2, 9, 7]) == 2, 'wrong result'


if __name__ == '__main__':
    test_num_triplets()
