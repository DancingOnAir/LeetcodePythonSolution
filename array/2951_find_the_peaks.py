from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] and mountain[i] > mountain[i + 1]]


def test_find_peaks():
    solution = Solution()
    assert solution.findPeaks([2, 4, 4]) == [], 'wrong result'
    assert solution.findPeaks([1, 4, 3, 8, 5]) == [1, 3], 'wrong result'


if __name__ == '__main__':
    test_find_peaks()
