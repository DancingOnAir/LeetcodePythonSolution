class Solution:
    def kmp(self, s, p):
        l1, l2 = len(s), len(p)

        nxt = [-1] * l2
        i, j = 0, -1
        while i < l2 - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                if p[i] == p[j]:
                    nxt[i] = nxt[j]
                else:
                    nxt[i] = j
            else:
                j = nxt[j]

        i, j = 0, 0
        while i < l1 and j < l2:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]

        if j == l2:
            return i - j
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        cur = a
        while len(cur) < len(b):
            cur += a
            res += 1
        cur += a

        # idx = cur.find(b)
        idx = self.kmp(cur, b)
        if idx == -1:
            return -1
        return res + 1 if idx + len(b) > len(a) * res else res


def test_repeated_string_match():
    solution = Solution()
    assert solution.repeatedStringMatch("abcd", "cdabcdab") == 3, 'wrong result'
    assert solution.repeatedStringMatch("a", "aa") == 2, 'wrong result'


if __name__ == '__main__':
    test_repeated_string_match()
