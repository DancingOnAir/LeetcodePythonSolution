from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        pass


def test_ways_to_reach_target():
    solution = Solution()
    assert solution.waysToReachTarget(6, [[6, 1], [3, 2], [2, 3]]) == 7, 'wrong result'
    assert solution.waysToReachTarget(5, [[50, 1], [50, 2], [50, 5]]) == 4, 'wrong result'
    assert solution.waysToReachTarget(18, [[6, 1], [3, 2], [2, 3]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_ways_to_reach_target()
