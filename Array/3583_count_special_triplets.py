from typing import List
from collections import defaultdict, Counter


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        suf = Counter(nums)
        pre = defaultdict(int)
        res = 0
        for x in nums:
            suf[x] -= 1
            res += pre[x * 2] * suf[x * 2]
            pre[x] += 1
        return res % (10 ** 9 + 7)


def test_special_triplets():
    solution = Solution()
    assert solution.specialTriplets([6, 3, 6]) == 1, 'wrong result'
    assert solution.specialTriplets([0, 1, 0, 0]) == 1, 'wrong result'
    assert solution.specialTriplets([8, 4, 2, 8, 4]) == 2, 'wrong result'


if __name__ == '__main__':
    test_special_triplets()
