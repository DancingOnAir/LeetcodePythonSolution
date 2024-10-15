class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel, consonant = 0, 0
        for ch in word:
            if ch.isalpha():
                if ch.lower() in 'aeiou':
                    vowel += 1
                else:
                    consonant += 1
            elif not ch.isdigit():
                return False
        return vowel >= 1 and consonant >= 1

    def isValid1(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel, consonant = False, False
        for c in word:
            cur = ord(c)
            if 48 <= cur <= 57:
                continue
            if 65 <= cur <= 90 or 97 <= cur <= 122:
                if c.lower() in 'aeiou':
                    vowel = True
                else:
                    consonant = True
            else:
                return False

        return vowel and consonant


def test_is_valid():
    solution = Solution()
    assert solution.isValid("234Adas"), 'wrong result'
    assert not solution.isValid("b3"), 'wrong result'
    assert not solution.isValid("a3$e"), 'wrong result'


if __name__ == '__main__':
    test_is_valid()
