from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res


def test_merge():
    solution = Solution()

    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals1))

    intervals2 = [[1, 4], [4, 5]]
    print(solution.merge(intervals2))

    intervals3 = [[1, 4], [2, 3]]
    print(solution.merge(intervals3))


if __name__ == '__main__':
    test_merge()
