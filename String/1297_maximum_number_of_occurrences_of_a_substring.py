from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = [0] * 26
        freq = defaultdict(int)
        start = 0
        unique = 0

        for i, c in enumerate(s):
            cnt[ord(c) - 97] += 1
            if cnt[ord(c) - 97] == 1:
                unique += 1

            if i - start + 1 > minSize:
                cnt[ord(s[start]) - 97] -= 1
                if cnt[ord(s[start]) - 97] == 0:
                    unique -= 1
                start += 1

            if i - start + 1 == minSize and unique <= maxLetters:
                freq[s[start:i+1]] += 1

        if not freq:
            return 0
        return max(freq.values())





def test_max_freq():
    solution = Solution()
    # assert solution.maxFreq('aababcaab', 2, 3, 4) == 2, 'wrong result'
    # assert solution.maxFreq('aaaa', 1, 3, 3) == 2, 'wrong result'
    assert solution.maxFreq('aabcabcab', 2, 2, 3) == 3, 'wrong result'
    assert solution.maxFreq('abcde', 2, 3, 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_freq()
