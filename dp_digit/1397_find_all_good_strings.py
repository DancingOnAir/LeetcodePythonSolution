from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        _kmp = self.kmp(evil)

        @lru_cache(None)
        def dp(idx, prefix_s1, prefix_s2, evil_matched_len):
            if evil_matched_len == len(evil):
                return 0
            if idx == n:
                return 1

            first = s1[idx] if prefix_s1 else 'a'
            last = s2[idx] if prefix_s2 else 'z'
            res = 0
            for i in range(ord(first), ord(last) + 1):
                c = chr(i)
                _prefix_s1 = prefix_s1 and s1[idx] == c
                _prefix_s2 = prefix_s2 and s2[idx] == c

                j = evil_matched_len
                while j and evil[j] != c:
                    j = _kmp[j - 1]

                if evil[j] == c:
                    j += 1

                res += dp(idx + 1, _prefix_s1, _prefix_s2, j)
            return res % (10 ** 9 + 7)

        return dp(0, True, True, 0)

    def kmp(self, pattern: str):
        tab = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j and pattern[i] != pattern[j]:
                j = tab[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            tab[i] = j
        return tab


def test_find_good_strings():
    solution = Solution()
    print(solution.kmp('ababac'))
    assert solution.findGoodStrings(2, 'aa', 'da', 'b') == 51, 'wrong result'
    assert solution.findGoodStrings(8, 'leetcode', 'leetgoes', 'leet') == 0, 'wrong result'
    assert solution.findGoodStrings(2, 'gx', 'gz', 'x') == 2, 'wrong result'


if __name__ == '__main__':
    test_find_good_strings()
