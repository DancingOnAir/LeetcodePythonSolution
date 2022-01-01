from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        freq = dict()
        for i, val in enumerate(arr):
            freq.setdefault(val, []).append(i)

        for k, vs in freq.items():
            for v in vs:
                res[v] = sum(abs(v - x) for x in vs if x != v)
        return res


def test_get_distances():
    solution = Solution()
    assert solution.getDistances([2, 1, 3, 1, 2, 3, 3]) == [4, 2, 7, 2, 4, 4, 5], 'wrong result'
    assert solution.getDistances([10, 5, 10, 10]) == [5, 0, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_get_distances()
