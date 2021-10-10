from collections import Counter


class Solution:
    # sliding window
    def characterReplacement(self, s: str, k: int) -> int:
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
