from collections import Counter, defaultdict


class Solution:
    # sliding window
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        if any(c[ch] < k for ch in 'abc'):
            return -1

        left = 0
        res = 0
        m = defaultdict(int)
        for right, ch in enumerate(s):
            m[ch] += 1
            while m[ch] + k > c[ch]:
                m[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return len(s) - res


def test_take_characters():
    solution = Solution()
    assert solution.takeCharacters("aabaaaacaabc", 2) == 8, 'wrong result'
    assert solution.takeCharacters("a", 1) == -1, 'wrong result'


if __name__ == '__main__':
    test_take_characters()
