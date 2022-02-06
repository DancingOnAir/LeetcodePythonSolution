from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ''


def test_first_palindrome():
    solution = Solution()
    assert solution.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada", 'wrong result'
    assert solution.firstPalindrome(["notapalindrome", "racecar"]) == "racecar", 'wrong result'
    assert solution.firstPalindrome(["def", "ghi"]) == "", 'wrong result'


if __name__ == '__main__':
    test_first_palindrome()
