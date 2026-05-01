class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        def helper(arr: list[int]) -> int:
            left, right = 0, len(nums) - 2
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > arr[mid + 1]:
                    right = mid
                else:
                    left = mid + 1
            return left

        i = helper(nums)
        s1 = sum(nums[:i])
        s2 = sum(nums[i + 1:])
        return -1 if s1 == s2 else int(s1 < s2)


def test_compare_bitonic_sums():
    solution = Solution()
    assert solution.compareBitonicSums([1, 3, 2, 1]) == 1, 'wrong result'
    assert solution.compareBitonicSums([2, 4, 5, 2]) == 0, 'wrong result'
    assert solution.compareBitonicSums([1, 2, 4, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_compare_bitonic_sums()
