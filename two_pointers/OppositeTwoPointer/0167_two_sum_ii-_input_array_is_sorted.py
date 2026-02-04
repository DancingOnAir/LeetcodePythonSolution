from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            elif s > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]


def test_two_sum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2], 'wrong result'
    assert solution.twoSum([2, 3, 4], 6) == [1, 3], 'wrong result'
    assert solution.twoSum([-1, 0], -1) == [1, 2], 'wrong result'


if __name__ == '__main__':
    test_two_sum()
