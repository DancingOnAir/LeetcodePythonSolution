from collections import Counter


class Solution:
    # 对于s[i:j] (j - i) mod k == 0 等价 i mod k == j mod k
    # 如果vowels == consonants, l = len(s[i:j]) (l * l) mod (4 * k) == 0
    # https://leetcode.cn/problems/count-beautiful-substrings-ii/solutions/2542274/fen-jie-zhi-yin-zi-qian-zhui-he-ha-xi-bi-ceil/
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # 计算需要的质因数个数
        def helper(x):
            ans = 1
            i = 2
            while i * i <= x:
                i2 = i * i
                while x % i2 == 0:
                    ans *= i
                    x //= i2
                if x % i == 0:
                    ans *= i
                    x //= i
                i += 1

            if x > 1:
                ans *= x
            return ans

        k = helper(k * 4)
        # (k - 1) mod k == -1 mod k
        cnt = Counter([(k - 1, 0)])
        res = ps = 0
        for i, c in enumerate(s):
            ps += 1 if c in 'aeiou' else -1
            p = (i % k, ps)
            res += cnt[p]
            cnt[p] += 1
        return res


def test_beautiful_substrings():
    solution = Solution()
    assert solution.beautifulSubstrings("baeyh", 2) == 2, 'wrong result'
    assert solution.beautifulSubstrings("abba", 1) == 3, 'wrong result'
    assert solution.beautifulSubstrings("bcdf", 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_beautiful_substrings()