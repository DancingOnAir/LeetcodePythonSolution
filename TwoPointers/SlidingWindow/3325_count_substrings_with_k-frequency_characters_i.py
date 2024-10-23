from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = l = 0
        cnt = Counter()
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] == k:
                cnt[s[l]] -= 1
                l += 1
            res += l
        return res

    def numberOfSubstrings1(self, s: str, k: int) -> int:
        n, l = len(s), 0
        # 计算所有的子串
        res = n * (n + 1) // 2
        cnt = Counter()
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[s[l]] -= 1
                l += 1
            # 排除不符合要求的子串
            res -= r - l + 1
        return res


def test_number_of_substrins():
    solution = Solution()
    assert solution.numberOfSubstrings("abacb", 2) == 4, 'wrong result'
    assert solution.numberOfSubstrings("abcde", 1) == 15, 'wrong result'


if __name__ == '__main__':
    test_number_of_substrins()
