from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        target = Counter(word2)
        match, left, res = len(target), 0, 0
        for right, ch in enumerate(word1):
            target[ch] -= 1
            match -= (target[ch] == 0)
            while match == 0:
                match += (target[word1[left]] == 0)
                target[word1[left]] += 1
                left += 1
            res += left

        return res

    def validSubstringCount1(self, word1: str, word2: str) -> int:
        target = Counter(word2)
        source = Counter()
        left = res = 0
        n = len(word1)
        for right, ch in enumerate(word1):
            source[ch] += 1
            while len(target - source) == 0:
                res += n - right
                source[word1[left]] -= 1
                left += 1

        return res


def test_valid_substring_count():
    solution = Solution()
    assert solution.validSubstringCount("bcca", "abc") == 1, 'wrong result'
    assert solution.validSubstringCount("abcabc", "abc") == 10, 'wrong result'
    assert solution.validSubstringCount("abcabc", "aaabc") == 0, 'wrong result'


if __name__ == '__main__':
    test_valid_substring_count()
