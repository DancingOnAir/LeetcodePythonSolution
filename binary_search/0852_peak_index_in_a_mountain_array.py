class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 2
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


def test_peak_index_in_mountain_array():
    solution = Solution()
    assert solution.peakIndexInMountainArray([0, 1, 0]) == 1, 'wrong result'
    assert solution.peakIndexInMountainArray([0, 2, 1, 0]) == 1, 'wrong result'
    assert solution.peakIndexInMountainArray([0, 10, 5, 2]) == 1, 'wrong result'


if __name__ == '__main__':
    test_peak_index_in_mountain_array()
