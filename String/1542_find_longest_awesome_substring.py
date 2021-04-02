from collections import Counter


class Solution:
    # https://leetcode.com/problems/find-longest-awesome-substring/discuss/785213/Example-Input-%223242415%22-Explanation-with-BitMask
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return s

        res, mask = 0, 0
        # here, 2^10 = 1024 coz only the string contains digits 0-9.
        memo = [-1] + [n] * 1023
        for i in range(n):
            mask ^= 1 << int(s[i])
            res = max(res, i - memo[mask])

            for j in range(10):
                check_mask = mask ^ (1 << j)
                res = max(res, i - memo[check_mask])
            memo[mask] = min(memo[mask], i)

        return res

    # TLE
    def longestAwesome1(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                ss = s[i:j]
                c = Counter(ss)
                if sum([1 for v in c.values() if (v & 0b1) == 1]) < 2:
                    res = max(res, len(ss))
        return res


def test_longest_awesome():
    solution = Solution()
    assert solution.longestAwesome('3242415') == 5, 'wrong result'
    assert solution.longestAwesome('12345678') == 1, 'wrong result'
    assert solution.longestAwesome('213123') == 6, 'wrong result'
    assert solution.longestAwesome('00') == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_awesome()
