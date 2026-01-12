from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(start, end):
            return abs(start[0] - end[0]) + abs(start[1] - end[1])

        man = dist([0, 0], target)
        for g in ghosts:
            if dist(g, target) <= man:
                return False
        return True


def test_escape_ghosts():
    solution = Solution()
    assert solution.escapeGhosts([[1, 0], [0, 3]], [0, 1]), 'wrong result'
    assert not solution.escapeGhosts([[1, 0]], [2, 0]), 'wrong result'
    assert not solution.escapeGhosts([[2, 0]], [1, 0]), 'wrong result'


if __name__ == '__main__':
    test_escape_ghosts()
