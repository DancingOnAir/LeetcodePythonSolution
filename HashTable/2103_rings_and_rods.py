from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        if n < 7:
            return 0

        freq = defaultdict(set)
        for i in range(0, n, 2):
            freq[rings[i+1]].add(rings[i])
        return sum(1 for v in freq.values() if len(v) == 3)


def test_count_points():
    solution = Solution()

    assert solution.countPoints('B0B6G0R6R0R6G9') == 1, 'wrong result'
    assert solution.countPoints('B0R0G0R9R0B0G0') == 1, 'wrong result'
    assert solution.countPoints('G4') == 0, 'wrong result'


if __name__ == '__main__':
    test_count_points()
