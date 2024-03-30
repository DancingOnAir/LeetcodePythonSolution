from typing import List
from heapq import heappop, heappush
from collections import Counter


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        res, hp = [], []
        count = Counter()
        for k, v in zip(nums, freq):
            count[k] += v
            heappush(hp, (-count[k], k))
            while count[hp[0][1]] != -hp[0][0]:
                heappop(hp)
            res.append(-hp[0][0])
        return res

    # TLE
    def mostFrequentIDs1(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = Counter()
        res = []
        for k, v in zip(nums, freq):
            cnt[k] += v
            res.append(cnt.most_common(1)[0][1])
        return res


def test_most_frequent_ids():
    solution = Solution()
    assert solution.mostFrequentIDs([2,3,2,1], [3,2,-3,1]) == [3,3,2,2], 'wrong result'
    assert solution.mostFrequentIDs([5,5,3], [2,-2,1]) == [2,0,1], 'wrong result'


if __name__ == '__main__':
    test_most_frequent_ids()
