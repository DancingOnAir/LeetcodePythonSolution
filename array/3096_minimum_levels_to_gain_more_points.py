from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        tot = sum(1 if x == 1 else -1 for x in possible)
        n, cur = len(possible), 0
        for i in range(n - 1):
            cur += (1 if possible[i] == 1 else -1)
            if 2 * cur > tot:
                return i + 1
        return -1


def test_minimum_levels():
    solution = Solution()
    assert solution.minimumLevels([1, 0, 1, 0]) == 1, 'wrong result'
    assert solution.minimumLevels([1, 1, 1, 1, 1]) == 3, 'wrong result'
    assert solution.minimumLevels([0, 0]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_levels()
