from typing import List
from collections import Counter, defaultdict


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c1 = Counter(nums)
        c2 = Counter(c1.values())
        for x in nums:
            if c2[c1[x]] == 1:
                return x
        return -1

    def firstUniqueFreq1(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        pos = defaultdict(int)
        for i, x in enumerate(nums):
            if x not in cnt:
                pos[x] = i
            cnt[x] += 1

        freq = defaultdict(list)
        for k, v in cnt.items():
            freq[v].append(k)

        res = -1
        for ks in freq.values():
            if len(ks) == 1:
                if res == -1:
                    res = pos[ks[0]]
                else:
                    res = min(res, pos[ks[0]])
        return nums[res] if res > -1 else res


def test_first_unique_freq():
    solution = Solution()
    assert solution.firstUniqueFreq([20, 10, 30, 30]) == 30, 'wrong result'
    assert solution.firstUniqueFreq([20, 20, 10, 30, 30, 30]) == 20, 'wrong result'
    assert solution.firstUniqueFreq([10, 10, 20, 20]) == -1, 'wrong result'


if __name__ == '__main__':
    test_first_unique_freq()
