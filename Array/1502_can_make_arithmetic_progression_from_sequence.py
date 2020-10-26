from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if d != arr[i] - arr[i - 1]:
                return False
        return True


def test_can_make_arithmetic_progression():
    solution = Solution()

    arr1 = [3, 5, 1]
    print(solution.canMakeArithmeticProgression(arr1))

    arr2 = [1, 2, 4]
    print(solution.canMakeArithmeticProgression(arr2))


if __name__ == '__main__':
    test_can_make_arithmetic_progression()
