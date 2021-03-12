class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s) // 2
        count1 = sum(1 for i in s[:mid] if i in vowels)
        count2 = sum(1 for i in s[mid:] if i in vowels)
        return count1 == count2


def test_haves_are_alike():
    solution = Solution()
    assert solution.halvesAreAlike('book'), 'wrong result'
    assert not solution.halvesAreAlike('textbook'), 'wrong result'
    assert not solution.halvesAreAlike('MerryChristmas'), 'wrong result'
    assert solution.halvesAreAlike('AbCdEfGh'), 'wrong result'


if __name__ == '__main__':
    test_haves_are_alike()
