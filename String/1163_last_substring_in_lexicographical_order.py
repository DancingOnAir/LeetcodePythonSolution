from collections import Counter


class Solution:
    # https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/362387/JavaPython-3-Two-short-O(n)-codes-language%3A-2-pointers-and-encoding.
    # encoding
    def lastSubstring(self, s: str) -> str:
        idx = {c: i for i, c in enumerate(sorted(set(s)))}
        radix, val, cur, lo = len(idx), 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            cur = idx[s[i]] + cur / radix
            if val <= cur:
                val = cur
                lo = i
        return s[lo:]

    # brute force but TLE
    def lastSubstring1(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        max_char = max(cnt)
        max_char_num = cnt[max_char]
        if max_char_num == n:
            return s

        for k in range(max_char_num, 0, -1):
            res = ''
            start = -1
            i = 0
            if max_char * k in s:
                while i <= max_char_num - k:
                    j = s.find(max_char, start + k)
                    if j == -1:
                        continue

                    if i > 0:
                        cur = s[start: j]

                        if res >= cur:
                            res += cur
                        else:
                            res = cur

                    start = j
                    i += 1

                if res < s[start:]:
                    res = s[start:]
                else:
                    res += s[start:]
                break

        return res


def test_last_substring():
    solution = Solution()

    assert solution.lastSubstring("xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji") == "zzwobllyxktqeibfoupcpptncggrdqbkji", 'wrong result'
    assert solution.lastSubstring('abab') == 'bab', 'wrong result'
    assert solution.lastSubstring('leetcode') == 'tcode', 'wrong result'


if __name__ == '__main__':
    test_last_substring()
