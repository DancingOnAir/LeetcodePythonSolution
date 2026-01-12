from itertools import permutations


class Solution:
    # kmp
    def minimumString(self, a: str, b: str, c: str) -> str:
        def kmp(s1, s2):
            if s2 in s1:
                return s1
            s = s1 + '#' + s2
            j = 0
            nxt = [0] * len(s)
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = nxt[j - 1]
                if s[i] == s[j]:
                    j += 1
                nxt[i] = j
            return s2 + s1[nxt[-1]:]
        return sorted([kmp(kmp(x, y), z) for x, y, z in permutations((a, b, c))], key=lambda x: (len(x), x))[0]

    def minimumString2(self, a: str, b: str, c: str) -> str:
        def merge(s1, s2):
            if s2 in s1:
                return s1

            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2

            return s1 + s2

        return sorted([merge(merge(x, y), z) for x, y, z in permutations((a, b, c))], key=lambda x: (len(x), x))[0]

    def minimumString1(self, a: str, b: str, c: str) -> str:
        def merge(s1, s2):
            if s2 in s1:
                return s1

            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2

            return s1 + s2

        res = sorted([merge(merge(a, b), c), merge(merge(b, a), c), merge(merge(c, b), a), merge(merge(b, c), a), merge(merge(a, c), b), merge(merge(c, a), b)], key=lambda x: (len(x), x))
        return res[0]


def test_minimum_string():
    solution = Solution()
    assert solution.minimumString("aba", "c", "b") == "abac", 'wrong result'
    assert solution.minimumString("ca", "a", "a") == "ca", 'wrong result'
    assert solution.minimumString("abc", "bca", "aaa") == "aaabca", 'wrong result'
    assert solution.minimumString("ab", "ba", "aba") == "aba", 'wrong result'


if __name__ == '__main__':
    test_minimum_string()
