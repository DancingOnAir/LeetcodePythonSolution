from collections import Counter


class Solution:
    # https://leetcode-cn.com/problems/number-of-wonderful-substrings/solution/qian-zhui-he-chang-jian-ji-qiao-by-endle-t57t/
    # pre sum + bit mask
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [1] + [0] * 1023
        res = cur = 0
        for w in word:
            cur ^= 1 << (ord(w) - ord('a'))
            res += cnt[cur]
            res += sum(cnt[cur ^ (1 << i)] for i in range(10))
            cnt[cur] += 1
        return res

    # brute force but TLE
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        if n < 2:
            return n

        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum(1 if v & 1 else 0 for v in Counter(word[i: j]).values()) > 1:
                    continue
                res += 1
        return res


def test_wonderful_substrings():
    solution = Solution()

    assert solution.wonderfulSubstrings("aba") == 4, 'wrong result'
    assert solution.wonderfulSubstrings("aabb") == 9, 'wrong result'
    assert solution.wonderfulSubstrings("he") == 2, 'wrong result'


if __name__ == '__main__':
    test_wonderful_substrings()
