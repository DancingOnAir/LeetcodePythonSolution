from math import ceil


class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        time, (begin, end) = 0, intervals[0]
        for l, r in intervals:
            if end < l:
                time += end - begin + 1
                begin, end = l, r
            elif end < r:
                end = r
        return (time + end - begin + 1) * ceil(brightness / 3)

    def minEnergy1(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        new_intervals = []
        for i in range(len(intervals)):
            if not new_intervals or new_intervals[-1][1] < intervals[i][0]:
                new_intervals.append(intervals[i])
            if new_intervals[-1][1] >= intervals[i][1]:
                continue
            new_intervals[-1][1] = intervals[i][1]

        q, r = divmod(brightness, 3)
        if r > 0:
            q += 1

        return sum(b - a + 1 for a, b in new_intervals) * q


def test_min_energy():
    solution = Solution()
    assert solution.minEnergy(5, brightness=5, intervals=[[6, 12]]) == 14, 'wrong result'
    assert solution.minEnergy(2, brightness=1, intervals=[[0, 0], [2, 2]]) == 2, 'wrong result'
    assert solution.minEnergy(4, brightness=2, intervals=[[1, 3], [2, 4]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_energy()
