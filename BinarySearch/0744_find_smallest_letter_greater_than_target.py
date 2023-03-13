from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left ,right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1

        return letters[left] if left < len(letters) else letters[0]


def test_next_greatest_letter():
    solution = Solution()
    assert solution.nextGreatestLetter(["c", "f", "j"], "a") == "c", 'wrong result'
    assert solution.nextGreatestLetter(["c", "f", "j"], "c") == "f", 'wrong result'
    assert solution.nextGreatestLetter(["x", "x", "y", "y"], "z") == "x", 'wrong result'


if __name__ == '__main__':
    test_next_greatest_letter()
