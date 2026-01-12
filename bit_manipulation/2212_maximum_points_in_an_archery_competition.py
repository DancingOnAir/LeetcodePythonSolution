from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        # effects = sorted((i / (v+1), i, v) for i, v in enumerate(aliceArrows))
        res = [0] * 12
        max_score = -1
        for i in range(1 << 12):
            score = arrow = 0
            bob = [0] * 12
            for j, v in enumerate(aliceArrows):
                if i >> j & 1:
                    score += j
                    arrow += v + 1
                    bob[j] = v + 1

                if arrow > numArrows:
                    continue

                if score > max_score:
                    max_score = score
                    bob[0] += numArrows - arrow
                    res = bob[:]
        return res


def test_maximum_bob_points():
    solution = Solution()
    assert solution.maximumBobPoints(9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]) == [0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1], 'wrong result'
    assert solution.maximumBobPoints(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 'wrong result'


if __name__ == '__main__':
    test_maximum_bob_points()
