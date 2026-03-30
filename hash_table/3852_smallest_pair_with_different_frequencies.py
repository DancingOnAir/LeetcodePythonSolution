from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt1 = Counter(nums)
        cnt2 = Counter()
        x = y = -1
        for k in sorted(cnt1):
            v = cnt1[k]
            if v not in cnt2 or k < cnt2[v]:
                cnt2[v] = k
                if x == -1 or x > k:
                    y = x
                    x = k
                elif y == -1 or y > k:
                    y = k
        return [-1, -1] if y == -1 else [x, y]


def test_min_distinct_freq_pair():
    solution = Solution()
    assert solution.minDistinctFreqPair([4,1]) == [-1,-1], 'wrong result'
    assert solution.minDistinctFreqPair([1,1,2,2,3,4]) == [1,3], 'wrong result'
    assert solution.minDistinctFreqPair([1,5]) == [-1,-1], 'wrong result'
    assert solution.minDistinctFreqPair([7]) == [-1,-1], 'wrong result'


if __name__ == '__main__':
    test_min_distinct_freq_pair()
