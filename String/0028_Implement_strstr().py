class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        j = 0
        nxt = [0] * m
        for i in range(1, m):
            while j and needle[i] != needle[j]:
                j = nxt[j - 1]
            if needle[i] == needle[j]:
                j += 1
            nxt[i] = j

        print(nxt)
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1


def test_strstr():
    solution = Solution()

    assert solution.strStr('hello', 'll') == 2, 'wrong result'
    assert solution.strStr('aaaaa', 'bba') == -1, 'wrong result'
    assert solution.strStr('', '') == 0, 'wrong result'


if __name__ == '__main__':
    test_strstr()
