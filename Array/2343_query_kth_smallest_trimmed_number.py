from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = list()
        trimmed = dict()
        for k, t in queries:
            trimmed.setdefault(t, sorted([s[-t:], i] for i, s in enumerate(nums)))
            res.append(trimmed[t][k - 1][1])
        return res

    def smallestTrimmedNumbers1(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = list()
        m = dict()
        for k, t in queries:
            if t not in m:
                m[t] = sorted([s[-t:], i] for i, s in enumerate(nums))
            res.append(m[t][k - 1][1])
        return res


def test_smallest_trimmed_numbers():
    solution = Solution()
    assert solution.smallestTrimmedNumbers(["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]]) == [2, 2, 1,
                                                                                                               0]
    assert solution.smallestTrimmedNumbers(["24", "37", "96", "04"], [[2, 1], [2, 2]]) == [3, 0]


if __name__ == '__main__':
    test_smallest_trimmed_numbers()
