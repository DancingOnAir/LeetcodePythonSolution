from collections import Counter, defaultdict


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt, last = Counter(s), []
        mx = max(cnt.values())
        for ch in s[::-1]:
            if cnt[ch] == mx:
                last.append(ch)
                cnt[ch] -= 1
        return ''.join(last[::-1])

    def lastNonEmptyString1(self, s: str) -> str:
        freq = defaultdict(int)
        last = defaultdict(int)
        max_freq = 0
        for i, ch in enumerate(s):
            freq[ch] += 1
            last[ch] = i
            max_freq = max(max_freq, freq[ch])

        res = []
        for k, v in freq.items():
            if v == max_freq:
                res.append((last[k], k))
        return ''.join([k for _, k in sorted(res)])


def test_last_non_empty_string():
    solution = Solution()
    assert solution.lastNonEmptyString("aabcbbca") == "ba", 'wrong result'
    assert solution.lastNonEmptyString("abcd") == "abcd", 'wrong result'


if __name__ == '__main__':
    test_last_non_empty_string()
