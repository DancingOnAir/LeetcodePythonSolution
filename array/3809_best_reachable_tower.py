from typing import List


class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx, cy = center
        m = [(q, x, y) for x, y, q in towers if abs(x - cx) + abs(y - cy) <= radius]
        if not m:
            return [-1, -1]
        _, x, y = max(m, key=lambda t: (t[0], -t[1], -t[2]))
        return [x, y]

    def bestTower1(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        res = [-1, -1]
        mx = -1
        for x, y, q in towers:
            if abs(center[0] - x) + abs(center[1] - y) <= radius:
                if q > mx:
                    mx = q
                    res = [x, y]
                elif q == mx:
                    res = min(res, [x, y])
        return res


def test_best_tower():
    solution = Solution()
    assert solution.bestTower([[1, 2, 5], [2, 1, 7], [3, 1, 9]], center=[1, 1], radius=2) == [3, 1], "wrong result"
    assert solution.bestTower([[1, 3, 4], [2, 2, 4], [4, 4, 7]], center=[0, 0], radius=5) == [1, 3], "wrong result"
    assert solution.bestTower([[5, 6, 8], [0, 3, 5]], center=[1, 2], radius=1) == [-1, -1], "wrong result"


if __name__ == '__main__':
    test_best_tower()
