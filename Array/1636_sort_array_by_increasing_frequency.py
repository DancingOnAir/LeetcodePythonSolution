from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = list()
        for k, v in sorted(dict(Counter(nums)).items(), key=lambda x: (x[1], -x[0])):
            res += [k] * v
        return res


def test_frequency_sort():
    solution = Solution()

    nums1 = [1, 1, 2, 2, 2, 3]
    res1 = [3, 1, 1, 2, 2, 2]
    assert solution.frequencySort(nums1) == res1, "wrong result"

    nums2 = [2, 3, 1, 3, 2]
    res2 = [1, 3, 3, 2, 2]
    assert solution.frequencySort(nums2) == res2, "wrong result"

    nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    res3 = [5, -1, 4, 4, -6, -6, 1, 1, 1]
    assert solution.frequencySort(nums3) == res3, "wrong result"


if __name__ == '__main__':
    test_frequency_sort()
