from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start, end = meetings[0][0], meetings[0][1]
        for i in range(len(meetings) - 1):
            if end < meetings[i + 1][0]:
                days -= end - start + 1
                start, end = meetings[i + 1][0], meetings[i + 1][1]
            else:
                end = max(end, meetings[i + 1][1])
        return days - (end - start + 1)


def test_count_days():
    solution = Solution()
    assert solution.countDays(57, [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48],
                                   [3, 31]]) == 1, 'wrong result'
    assert solution.countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2, 'wrong result'
    assert solution.countDays(5, [[2, 4], [1, 3]]) == 1, 'wrong result'
    assert solution.countDays(6, [[1, 6]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_days()
