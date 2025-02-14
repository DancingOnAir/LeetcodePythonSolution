from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = 0
        circles.sort(key=lambda c: -c[2])
        max_x = max(c[0] + c[2] for c in circles)
        max_y = max(c[1] + c[2] for c in circles)
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                for x, y, r in circles:
                    if (x - i) ** 2 + (y - j) ** 2 <= r * r:
                        res += 1
                        break
        return res


def test_count_lattice_points():
    solution = Solution()
    assert solution.countLatticePoints([[2, 2, 1]]) == 5, 'wrong result'
    assert solution.countLatticePoints([[2, 2, 2], [3, 4, 1]]) == 16, 'wrong result'


if __name__ == '__main__':
    test_count_lattice_points()
