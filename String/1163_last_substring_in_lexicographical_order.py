from collections import Counter


class Solution:
    def lastSubstring(self, s: str) -> str:
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
