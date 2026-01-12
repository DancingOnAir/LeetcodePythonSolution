from collections import Counter


class Solution:
    # sliding window
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        i = 0
        cnt = {c: 0 for c in 'abc'}
        for c in s:
            cnt[c] += 1
            while all(cnt.values()):
                cnt[s[i]] -= 1
                i += 1
            res += i
        return res

    # https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise
    def numberOfSubstrings2(self, s: str) -> int:
        res = 0
        last = [-1] * 3
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            res += min(last) + 1
        return res

    # brute force
    def numberOfSubstrings1(self, s: str) -> int:
        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if len(Counter(s[i: j])) == 3:
                    res += 1

        return res


def test_number_of_substrings():
    solution = Solution()
    assert solution.numberOfSubstrings('abcabc') == 10, 'wrong result'
    assert solution.numberOfSubstrings('aaacb') == 3, 'wrong result'
    assert solution.numberOfSubstrings('abc') == 1, 'wrong result'


if __name__ == '__main__':
    test_number_of_substrings()
