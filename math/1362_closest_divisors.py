from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int((num + 2) ** 0.5), 0, -1):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]


def test_closest_divisors():
    solution = Solution()
    assert solution.closestDivisors(8) == [3, 3], 'wrong result'
    assert solution.closestDivisors(123) == [5, 25], 'wrong result'
    assert solution.closestDivisors(999) == [25, 40], 'wrong result'


if __name__ == '__main__':
    test_closest_divisors()
