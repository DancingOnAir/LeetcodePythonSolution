from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
            pairs += (1 if cnt[x] % 2 == 0 else 0)

        return [pairs, len(nums) - pairs * 2]

    def numberOfPairs1(self, nums: List[int]) -> List[int]:
        a = b = 0
        for v in Counter(nums).values():
            a += v // 2
            b += v % 2
        return [a, b]


def test_number_of_pairs():
    solution = Solution()
    assert solution.numberOfPairs([1, 3, 2, 1, 3, 2, 2]) == [3, 1], 'wrong result'
    assert solution.numberOfPairs([1, 1]) == [1, 0], 'wrong result'


if __name__ == '__main__':
    test_number_of_pairs()
