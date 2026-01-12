from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        pre = -1
        cnt = 0
        for s, e in sorted(ranges):
            if s > pre:
                cnt += 1
            pre = max(pre, e)

        return (2 ** cnt) % (10 ** 9 + 7)


def test_count_ways():
    solution = Solution()
    assert solution.countWays([[0,0],[8,9],[12,13],[1,3]]) == 16, 'wrong result'
    assert solution.countWays([[1,3],[10,20],[2,5],[4,8]]) == 4, 'wrong result'
    assert solution.countWays([[6, 10], [5, 15]]) == 2, 'wrong result'
    assert solution.countWays([[1, 3], [10, 20], [2, 5], [4, 8]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_ways()
