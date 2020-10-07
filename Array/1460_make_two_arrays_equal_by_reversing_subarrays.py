from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


def test_can_be_equal():
    solution = Solution()

    target1 = [1, 2, 3, 4]
    arr1 = [2, 4, 1, 3]
    print(solution.canBeEqual(target1, arr1))

    target2 = [7]
    arr2 = [7]
    print(solution.canBeEqual(target2, arr2))

    target3 = [1, 12]
    arr3 = [12, 1]
    print(solution.canBeEqual(target3, arr3))

    target4 = [3, 7, 9]
    arr4 = [3, 7, 11]
    print(solution.canBeEqual(target4, arr4))

    target5 = [1, 1, 1, 1, 1]
    arr5 = [1, 1, 1, 1, 1]
    print(solution.canBeEqual(target5, arr5))


if __name__ == '__main__':
    test_can_be_equal()





