from collections import defaultdict


class Solution:
    def numberOfSpecialChars1(self, word: str) -> int:
        lo, up = set(), set()
        for ch in word:
            if ch.islower():
                lo.add(ch)
            else:
                up.add(ch.lower())
        return len(lo & up)

    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        m = dict()
        for ch in word:
            if ch.islower() and ch.upper() in word and ch not in m:
                res += 1
                m[ch] = m.get(ch, 0)
        return res


def test_number_of_special_chars():
    solution = Solution()
    assert solution.numberOfSpecialChars("aaAbcBC") == 3, 'wrong result'
    assert solution.numberOfSpecialChars("abc") == 0, 'wrong result'
    assert solution.numberOfSpecialChars("abBCab") == 1, 'wrong result'


if __name__ == '__main__':
    test_number_of_special_chars()
