from collections import Counter


class Solution:
    # string
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xs = []
        ys = []
        others = []
        for c in s:
            if c == x:
                xs.append(x)
            elif c == y:
                ys.append(y)
            else:
                others.append(c)
        return ''.join(ys + others + xs)

    # hash table
    def rearrangeString1(self, s: str, x: str, y: str) -> str:
        cnt = Counter(s)
        if x not in cnt or y not in cnt:
            return s

        res = y * cnt[y]
        for c in s:
            if c == x or c == y:
                continue
            res += c
        return res + x * cnt[x]


def test_rearrange_string():
    solution = Solution()
    assert solution.rearrangeString("aabc", x = "a", y = "c") == "cbaa", 'wrong result'
    assert solution.rearrangeString("dcab", x = "d", y = "b") == "bcad", 'wrong result'
    assert solution.rearrangeString("axe", x = "o", y = "x") == "axe", 'wrong result'


if __name__ == '__main__':
    test_rearrange_string()
