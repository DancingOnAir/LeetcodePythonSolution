from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = max_freq = 0
        cnt = Counter()

        for i, c in enumerate(s):
            cnt[c] += 1
            max_freq = max(max_freq, cnt[c])

            if res < max_freq + k:
                res += 1
            else:
                cnt[s[i - res]] -= 1
        return res

    # sliding window
    def characterReplacement1(self, s: str, k: int) -> int:
        i = max_freq = 0
        cnt = Counter()

        for j, c in enumerate(s):
            cnt[c] += 1
            max_freq = max(max_freq, cnt[c])

            if j - i + 1 > max_freq + k:
                i += 1
                cnt[s[i]] -= 1
        return len(s) - i


def test_character_replacement():
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4, 'wrong result'
    assert solution.characterReplacement("AABABBA", 1) == 4, 'wrong result'


if __name__ == '__main__':
    test_character_replacement()
