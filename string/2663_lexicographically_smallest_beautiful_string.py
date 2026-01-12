class Solution:
    # 如果1个长度为m的字符串是回文字串，那么它中间长度为m-2的子串也一定是回文字串，所以该题只需要判断是否含有长度为2或3的回文字串。
    # 即s[i]左边是否存在,s[i - 1] == s[i] or s[i - 2] == s[i]
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        n = len(s)
        i = n - 1
        s = list(map(ord, s))
        s[i] += 1
        while i < n:
            if s[i] == k:
                if i == 0:
                    return ''
                s[i] = a
                i -= 1
                s[i] += 1
            elif i > 0 and s[i - 1] == s[i] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1
            else:
                # 检查后面的字符串是否形成回文字串
                i += 1
        return ''.join(map(chr, s))


def test_smallest_beautiful_string():
    solution = Solution()
    assert solution.smallestBeautifulString("abcz", 26) == "abda", 'wrong result'
    assert solution.smallestBeautifulString("dc", 4) == "", 'wrong result'


if __name__ == '__main__':
    test_smallest_beautiful_string()
