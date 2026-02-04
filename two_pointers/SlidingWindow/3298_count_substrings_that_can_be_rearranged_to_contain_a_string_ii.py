from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt = Counter(word2)
        l, res, match = 0, 0, len(cnt)
        for r, ch in enumerate(word1):
            cnt[ch] -= 1
            match -= (cnt[ch] == 0)

            while match == 0:
                match += (cnt[word1[l]] == 0)
                cnt[word1[l]] += 1
                l += 1
            res += l
        return res


def test_valid_substring_count():
    solution = Solution()
    assert solution.validSubstringCount("bcca", "abc") == 1, 'wrong result'
    assert solution.validSubstringCount("abcabc", "abc") == 10, 'wrong result'
    assert solution.validSubstringCount("abcabc", "aaabc") == 0, 'wrong result'


if __name__ == '__main__':
    test_valid_substring_count()
