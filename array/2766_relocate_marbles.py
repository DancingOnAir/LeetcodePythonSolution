from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        res = dict()
        for x in nums:
            res[x] = 1
        for i, x in enumerate(moveFrom):
            res.pop(x)
            res[moveTo[i]] = 1
        return sorted(res.keys())

    def relocateMarbles1(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        res = set(nums)
        for s, t in zip(moveFrom, moveTo):
            res.discard(s)
            res.add(t)
        return sorted(res)


def test_relocate_marbles():
    solution = Solution()
    assert solution.relocateMarbles([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]) == [5, 6, 8, 9], 'wrong result'
    assert solution.relocateMarbles([1, 1, 3, 3], [1, 3], [2, 2]) == [2], 'wrong result'


if __name__ == '__main__':
    test_relocate_marbles()
