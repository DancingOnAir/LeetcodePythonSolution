from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helper(x):
            i = 1
            while i * i <= x:
                if i * i == x:
                    cnt2[i] += cnt1[x]
                elif x % i == 0:
                    cnt2[i] += cnt1[x]
                    cnt2[x // i] += cnt1[x]
                i += 1

        res = 0
        cnt1, cnt2 = Counter(nums1), Counter()
        for x in cnt1:
            helper(x)

        for x in nums2:
            x *= k
            res += cnt2[x]
        return res


def test_number_of_pairs():
    solution = Solution()
    assert solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1) == 5, 'wrong result'
    assert solution.numberOfPairs([1, 2, 4, 12], [2, 4], 3) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_pairs()
