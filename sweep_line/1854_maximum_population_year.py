from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        endpoints = list()
        for s, e in logs:
            endpoints.append([s, 1])
            endpoints.append([e, -1])

        res = mx = cur = 0
        for i, val in sorted(endpoints):
            cur += val
            if mx < cur:
                mx = cur
                res = i

        return res


def test_maximum_population():
    solution = Solution()
    assert solution.maximumPopulation([[1993, 1999], [2000, 2010]]) == 1993, 'wrong result'
    assert solution.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960, 'wrong result'


if __name__ == '__main__':
    test_maximum_population()

