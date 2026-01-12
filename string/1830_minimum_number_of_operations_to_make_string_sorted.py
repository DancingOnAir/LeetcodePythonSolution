from functools import lru_cache


# https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-string-sorted/solution/shi-zi-fu-chuan-you-xu-de-zui-shao-cao-z-qgra/
# The operations of this question is to get the previous lexicographical order string
class Solution:
    # 用到的数论知识
    # 1.欧拉函数(Euler's totient function), 对于正整数n, 欧拉函数是小于等于n的正整数中与n互质的数的数目,记做φ(n) eg. φ(1)=1，φ(8)=4
    # 2.费马小定理, 互质的2个正整数a和n，有a^φ(n) ≡ 1 (mod n)
    # 3.特别的, 如果正整数n为质数，那么φ(n) = n - 1, 则有a^(n - 1) ≡ 1 (mod n)
    # 4.该题用到的技巧:
    #   a.  2个正整数a，b和取模用的质数m = 10 ** 9 + 7 求 (a^b) % m
    #       这里m为质数,那么φ(m) = m - 1 = 10 ** 9 + 6, 假设b = k * 1_000_000_006 + r (k, r均为整数，k是商，r是余数)
    #       那么 (a^b) % m = (a^(k * 1_000_000_006 + r)) % m = ((a^1_000_000_006)^k) % m * (a^r) % m = (a^r) % m
    #   b.  乘法逆元，正整数a，存在另一个正整数b (0 < b < m), 满足 (a*b) % m = 1, 则称b为a的逆元
    #       如何求b，利用费马小定理 a^(m - 1) ≡ 1 (mod m), 有a^(m - 1) * b ≡ b, 可以推出a^(m - 2) * (a * b) ≡ b, 即a^(m - 2) ≡ b
    def makeStringSorted(self, s: str) -> int:
        # 求阶乘i!
        @lru_cache(None)
        def f(i):
            return 1 if i <= 1 else (f(i - 1) * i) % MOD

        @lru_cache(None)
        def inverse(i):
            return pow(i, MOD - 2, MOD)

        MOD, n, res = 1_000_000_007, len(s), 0
        cnt = [0] * 26

        for i, c in enumerate(s[::-1]):
            idx = ord(c) - ord('a')
            cnt[idx] += 1

            ans = sum(cnt[:idx]) * f(i)
            for j in range(26):
                ans *= inverse(f(cnt[j])) % MOD
            res += ans
        return res % MOD

    # https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/discuss/1163050/Python-O(26n)-math-solution-explained
    def makeStringSorted1(self, s: str) -> int:
        cnt, tot, res, combination_tot = [0] * 26, 0, 0, 1
        for c in s[::-1]:
            idx = ord(c) - 97
            cnt[idx] += 1
            tot += 1

            # eg. 'cdbea' for i == 0, choose 'a' or 'b' is less than 'c', so permutation num is 2 * 4!
            # we can derive that
            # for i, permutation num = sum(cnt[:idx]) * (tot - 1)! / cnt[0]! * cnt[1]! * ... * cnt[25]!
            # equals (sum(cnt[:idx]) / tot) * (tot! / cnt[0]! * cnt[1]! * ... * cnt[25]!)
            combination_tot = combination_tot * tot // cnt[idx]
            res += combination_tot * sum(cnt[:idx]) // tot
        return res % (10 ** 9 + 7)


def test_make_string_sorted():
    solution = Solution()
    assert solution.makeStringSorted('cba') == 5, 'wrong result'
    assert solution.makeStringSorted('aabaa') == 2, 'wrong result'
    assert solution.makeStringSorted('cdbea') == 63, 'wrong result'
    assert solution.makeStringSorted('leetcodeleetcodeleetcode') == 982157772, 'wrong result'


if __name__ == '__main__':
    test_make_string_sorted()
