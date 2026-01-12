from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        for k1, v1 in cnt1.items():
            q, r = divmod(k1, k)
            if r == 0:
                for k2, v2 in cnt2.items():
                    if q % k2 == 0:
                        res += v1 * v2
        return res


def test_number_of_pairs():
    solution = Solution()
    assert solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1) == 5, 'wrong result'
    assert solution.numberOfPairs([1, 2, 4, 12], [2, 4], 3) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_pairs()
