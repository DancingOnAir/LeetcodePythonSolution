from collections import Counter


class Solution:
    # https://leetcode-cn.com/problems/last-substring-in-lexicographical-order/solution/c-shuang-zhi-zhen-ji-lu-zi-dian-xu-zui-d-ovwd/
    # 双指针，指针l记录字典序最大子串的首位下标，指针r向后扫描并与指针l进行比较
    # s[l] > s[r]：r指针后移
    # s[l] < s[r]：存在更大的子串，l移动到r，r指针后移
    # s[l] == s[r]：k = 1,2,3,....，此时比较s[l + k] 与 s[r + k]，直到出现两者不相等的情况
    # s[l + k] < s[r + k]: l移动到r，r指针后移
    # s[l + k] > s[r + k]: l不动，r移动到r + k + 1
    def lastSubstring(self, s: str) -> str:
        i, j, k, n = 0, 1, 0, len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i] < s[j + k]:
                i = j + k
                j = i + 1
                k = 0
            elif s[i + k] < s[j + k]:
                i = j
                j += 1
                k = 0
            else:
                j += 1
                k = 0
        return s[i:]


    # 1.排序最后的字符串必然是从某个位置一直到字符串结束
    # 2.排序最后的字符串必然是以最大的字符开始
    def lastSubstring3(self, s: str) -> str:
        max_char = max(s)
        res = ''
        for i, c in enumerate(s):
            if c == max_char and s[i:] > res:
                res = s[i:]
        return res

    # https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/362387/JavaPython-3-Two-short-O(n)-codes-language%3A-2-pointers-and-encoding.
    # encoding
    def lastSubstring2(self, s: str) -> str:
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
