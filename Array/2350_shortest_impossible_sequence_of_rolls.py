from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        pass


def test_shortest_sequence():
    solution = Solution()
    assert solution.shortestSequence([4, 2, 1, 2, 3, 3, 2, 4, 1], 4) == 3, 'wrong result'
    assert solution.shortestSequence([1, 1, 2, 2], 2) == 2, 'wrong result'
    assert solution.shortestSequence([1, 1, 3, 2, 2, 2, 3, 3], 4) == 1, 'wrong result'


if __name__ == '__main__':
    test_shortest_sequence()
