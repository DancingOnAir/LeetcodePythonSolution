from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        start, end = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < start:
                left += i,
            elif i[0] > end:
                right += i,
            else:
                start = min(start, i[0])
                end = max(end, i[1])

        return left + [[start, end]] + right

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals += newInterval,
        for i in sorted(intervals, key=lambda x: (x[0], x[1])):
            if res and res[-1][-1] >= i[0]:
                res[-1][-1] = max(res[-1][-1], i[1])
            else:
                res += i,

        return res


def test_insert():
    solution = Solution()

    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    print(solution.insert(intervals1, newInterval1))

    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    print(solution.insert(intervals2, newInterval2))


if __name__ == '__main__':
    test_insert()
