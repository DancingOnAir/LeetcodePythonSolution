from typing import List
from collections import defaultdict, Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq, res = Counter(nums), 0
        for val in freq:
            res += min(freq[val], freq[k - val])
        return res // 2

    def maxOperations1(self, nums: List[int], k: int) -> int:
        res = 0
        freq = defaultdict(int)
        for x in nums:
            if x in freq and freq[x] > 0:
                freq[x] -= 1
                res += 1
            else:
                freq[k - x] += 1
        return res


def test_max_operations():
    solution = Solution()
    assert solution.maxOperations([1, 2, 3, 4], 5) == 2, 'wrong result'
    assert solution.maxOperations([3, 1, 3, 4, 3], 6) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_operations()
