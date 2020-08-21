from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for i in sorted(intervals, key=lambda x: (x[0], x[1])):
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res += i,
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
