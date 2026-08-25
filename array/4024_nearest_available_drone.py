class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        res = -1
        min_dist = float('inf')
        for i, (x, y, r) in enumerate(drones):
            d = abs(x - target[0]) + abs(y - target[1])
            if d <= r:
                if min_dist > d:
                    min_dist = d
                    res = i
        return res


def test_nearest_drone():
    solution = Solution()
    assert solution.nearestDrone([[0, 0, 8], [2, 2, 9]], target=[3, 4]) == 1, 'wrong result'
    assert solution.nearestDrone([[2, 1, 5], [4, 4, 5], [6, 6, 8]], target=[5, 5]) == 1, 'wrong result'
    assert solution.nearestDrone([[4, 4, 5]], target=[8, 6]) == -1, 'wrong result'


if __name__ == '__main__':
    test_nearest_drone()
