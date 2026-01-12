from typing import List
from collections import Counter


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        res = float('inf')
        k1 = sorted(cnt1)
        k2 = sorted(cnt2)
        s1= set(k1)
        for x in k1:
            cur = k2[0] - x
            if all(((y - cur) in s1) and cnt2[y] <= cnt1[y - cur] for y in k2):
                res = min(res, cur)
        return res


def test_minimum_added_integer():
    solution = Solution()
    assert solution.minimumAddedInteger([10,2,8,7,5,6,7,10], [5,8,5,3,8,4]) == -2, 'wrong result'
    assert solution.minimumAddedInteger([4, 20, 16, 12, 8], [14, 18, 10]) == -2, 'wrong result'
    assert solution.minimumAddedInteger([3, 5, 5, 3], [7, 7]) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_added_integer()
