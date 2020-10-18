from typing import List
from collections import Counter


class Solution:
    def validate(self, bloomDay: List[int], m: int, k: int, day: int):
        count = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] > day:
                m -= count // k
                count = 0
            else:
                count += 1
        m -= count // k
        return m == 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        total = m * k
        if total > n:
            return -1

        hash_map = Counter(bloomDay)
        for key in sorted(hash_map):
            total -= hash_map[key]
            if total <= 0:
                if k == 1 or self.validate(bloomDay, m, k, key):
                    return key

        return -1


def test_min_days():
    solution = Solution()

    bloomDay1 = [1, 10, 3, 10, 2]
    m1 = 3
    k1 = 1
    print(solution.minDays(bloomDay1, m1, k1))

    bloomDay2 = [1, 10, 3, 10, 2]
    m2 = 3
    k2 = 2
    print(solution.minDays(bloomDay2, m2, k2))

    bloomDay3 = [7, 7, 7, 7, 12, 7, 7]
    m3 = 2
    k3 = 3
    print(solution.minDays(bloomDay3, m3, k3))

    bloomDay4 = [1000000000, 1000000000]
    m4 = 1
    k4 = 1
    print(solution.minDays(bloomDay4, m4, k4))

    bloomDay5 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    m5 = 4
    k5 = 2
    print(solution.minDays(bloomDay5, m5, k5))


if __name__ == '__main__':
    test_min_days()
