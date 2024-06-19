from typing import List
from collections import Counter


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter(x % 24 for x in hours)
        res = (cnt[0] - 1) * cnt[0] // 2 + (cnt[12] - 1) * cnt[12] // 2
        for i in range(1, 12):
            res += cnt[24 - i] * cnt[i]
        return res


def test_count_complete_day_pairs():
    solution = Solution()
    assert solution.countCompleteDayPairs([3, 17, 19, 18, 1, 16, 18, 9, 21, 21, 17, 3, 13, 12, 2]) == 4, 'wrong result'
    assert solution.countCompleteDayPairs([1, 16]) == 0, 'wrong result'
    assert solution.countCompleteDayPairs([12, 12, 30, 24, 24]) == 2, 'wrong result'
    assert solution.countCompleteDayPairs([72, 48, 24, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_complete_day_pairs()
