from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        memo = set()
        for c in permutations(sorted(arr), 4):
            memo.add(c)

        for m in sorted(list(memo), reverse=True):
            if 0 <= m[0] * 10 + m[1] < 24 and 0 <= m[2] * 10 + m[3] < 60:
                return str(m[0]) + str(m[1]) + ':' + str(m[2]) + str(m[3])
        return ""


def test_largest_time_from_digits():
    solution = Solution()

    assert solution.largestTimeFromDigits([2, 0, 6, 6]) == "06:26", 'wrong result'
    assert solution.largestTimeFromDigits([1, 2, 3, 4]) == "23:41", 'wrong result'
    assert solution.largestTimeFromDigits([5, 5, 5, 5]) == "", 'wrong result'
    assert solution.largestTimeFromDigits([0, 0, 0, 0]) == "00:00", 'wrong result'
    assert solution.largestTimeFromDigits([0, 0, 1, 0]) == "10:00", 'wrong result'


if __name__ == '__main__':
    test_largest_time_from_digits()
