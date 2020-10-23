from typing import List
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminders = defaultdict(int)
        for a in arr:
            reminders[a % k] += 1

        for key in sorted(reminders):
            if not key and (reminders[key] & 1):
                return False

            if key and reminders[key] != reminders[k - key]:
                return False

        return True


def test_can_arrange():
    solution = Solution()

    arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    k1 = 5
    print(solution.canArrange(arr1, k1))

    arr2 = [1, 2, 3, 4, 5, 6]
    k2 = 7
    print(solution.canArrange(arr2, k2))

    arr3 = [1, 2, 3, 4, 5, 6]
    k3 = 10
    print(solution.canArrange(arr3, k3))

    arr4 = [-10, 10]
    k4 = 2
    print(solution.canArrange(arr4, k4))

    arr5 = [-1, 1, -2, 2, -3, 3, -4, 4]
    k5 = 3
    print(solution.canArrange(arr5, k5))


if __name__ == '__main__':
    test_can_arrange()
