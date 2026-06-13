from itertools import pairwise


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for x, y in pairwise(s):
            if abs(ord(x) - ord(y)) > 2:
                return False
        return True


def test_is_adjacent_diff_at_most_two():
    solution = Solution()
    assert solution.isAdjacentDiffAtMostTwo("132"), 'wrong result'
    assert not solution.isAdjacentDiffAtMostTwo("129"), 'wrong result'


if __name__ == '__main__':
    test_is_adjacent_diff_at_most_two()
