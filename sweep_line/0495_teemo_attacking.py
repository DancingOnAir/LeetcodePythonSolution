from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(duration, timeSeries[i] - timeSeries[i - 1])
        return res + duration


def test_find_poisoned_duration():
    solution = Solution()
    assert solution.findPoisonedDuration([1, 4], 2) == 4, 'wrong result'
    assert solution.findPoisonedDuration([1, 2], 2) == 3, 'wrong result'


if __name__ == '__main__':
    test_find_poisoned_duration()
