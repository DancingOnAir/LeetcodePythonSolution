class Solution:
    # kmp
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2 = len(haystack), len(needle)
        i, j = 0, -1
        # generate next array
        nxt = [-1] * l2
        while i < l2 - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                if needle[i] == needle[j]:
                    nxt[i] = nxt[j]
                else:
                    nxt[i] = j
            else:
                j = nxt[j]
        # compare
        i, j = 0, 0
        while i < l1 and j < l2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]

        if j == l2:
            return i - j
        return -1


def test_str_str():
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0, 'wrong result'
    assert solution.strStr("leetcode", "leeto") == -1, 'wrong result'


if __name__ == '__main__':
    test_str_str()
