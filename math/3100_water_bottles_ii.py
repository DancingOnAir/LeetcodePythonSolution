class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            r = int((((2 * numExchange - 1) ** 2 + numBottles * 8) ** 0.5 - 1) // 2)
            n = r - numExchange + 1
            numBottles -= (numExchange + r) * n // 2
            numBottles += n
            res += n
            numExchange = r + 1

        return res


def test_max_bottles_drunk():
    solution = Solution()
    assert solution.maxBottlesDrunk(13, 6) == 15, 'wrong result'
    assert solution.maxBottlesDrunk(10, 3) == 13, 'wrong result'


if __name__ == '__main__':
    test_max_bottles_drunk()
