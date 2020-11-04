from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0

        left, right = 0, n - 1
        while left < right and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        res = min(n - left - 1, right)
        for i in range(left + 1):
            if arr[i] <= arr[right]:
                res = min(res, right - i - 1)
            elif right < n - 1:
                right += 1
            else:
                break
        return res



def test_find_length_of_shortest_subarray():
    solution = Solution()

    arr1 = [1, 2, 3, 10, 0, 7, 8, 9]
    print(solution.findLengthOfShortestSubarray(arr1))
    assert solution.findLengthOfShortestSubarray(arr1) == 2, "error result"

    arr2 = [5, 4, 3, 2, 1]
    print(solution.findLengthOfShortestSubarray(arr2))
    assert solution.findLengthOfShortestSubarray(arr2) == 4, "error result"

    arr3 = [1, 2, 3]
    print(solution.findLengthOfShortestSubarray(arr3))
    assert solution.findLengthOfShortestSubarray(arr3) == 0, "error result"

    arr4 = [1]
    print(solution.findLengthOfShortestSubarray(arr4))
    assert solution.findLengthOfShortestSubarray(arr4) == 0, "error result"

    arr5 = [2, 2, 2, 1, 1, 1]
    print(solution.findLengthOfShortestSubarray(arr5))
    assert solution.findLengthOfShortestSubarray(arr5) == 3, "error result"


if __name__ == '__main__':
    test_find_length_of_shortest_subarray()
