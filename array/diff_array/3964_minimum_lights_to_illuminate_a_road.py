class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        d = [0] * (n + 1)
        for i, x in enumerate(lights):
            if x > 0:
                d[max(0, i - x)] += 1
                d[min(i + x + 1, n)] -= 1

        res = sum_d = 0
        for i in range(n):
            sum_d += d[i]
            if sum_d == 0:
                res += 1
                sum_d += 1
                d[min(i + 3, n)] -= 1
        return res


def test_min_lights():
    solution = Solution()
    assert solution.minLights([0, 0, 0]) == 1, "wrong result"
    assert solution.minLights([0, 0, 0, 0]) == 2, "wrong result"
    assert solution.minLights([0, 0, 0, 2, 0]) == 1, "wrong result"


if __name__ == "__main__":
    test_min_lights()
