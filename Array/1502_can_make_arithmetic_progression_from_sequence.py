from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val = min(arr)
        gap = (max(arr) - min_val) / (len(arr) - 1)
        if not gap:
            return True

        s = set(num - min_val for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)

    def canMakeArithmeticProgression1(self, arr: List[int]) -> bool:
        arr.sort()
        gap = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if gap != arr[i] - arr[i - 1]:
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
