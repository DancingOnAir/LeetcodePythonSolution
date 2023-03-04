from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left <= right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid - 1
        return arr[left: left + k]


def test_find_closest_elements():
    solution = Solution()
    assert solution.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10], 'wrong result'
    assert solution.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4], 'wrong result'
    assert solution.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_find_closest_elements()
