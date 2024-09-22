class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = ''
        for i, num in enumerate(map(lambda x: ord(x) - 97, s)):
            dist = min(num, 26 - num)
            if dist <= k:
                k -= dist
                res += 'a'
            else:
                res += chr(num + 97 - k)
                break
        return res + s[i + 1:]

    def getSmallestString1(self, s: str, k: int) -> str:
        res = []
        i = 0
        while k > 0 and i < len(s):
            ch = s[i]
            a = ord(ch) - ord('a')
            b = ord('a') + 26 - ord(ch)

            if k < b <= a or k < a <= b:
                res.append(chr(ord(ch) - k))
                k = 0
            elif a < b:
                res.append('a')
                k -= a
            else:
                res.append('a')
                k -= b
            i += 1
        return ''.join(res) + s[i:]


def test_get_smallest_string():
    solution = Solution()
    assert solution.getSmallestString("xaxcd", 4) == "aawcd", 'wrong result'
    assert solution.getSmallestString("zbbz", 3) == "aaaz", 'wrong result'
    assert solution.getSmallestString("lol", 0) == "lol", 'wrong result'


if __name__ == '__main__':
    test_get_smallest_string()
