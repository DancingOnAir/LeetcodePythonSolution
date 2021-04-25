class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if not n:
            return 0

        vowels = set('aeiou')
        pre_sum = [0]
        for c in s:
            pre_sum.append(pre_sum[-1] + (1 if c in vowels else 0))

        res = 0
        for i in range(k, n + 1):
            res = max(res, pre_sum[i] - pre_sum[i - k])
        return res


def test_max_vowels():
    solution = Solution()
    assert solution.maxVowels('weallloveyou', 7) == 4, 'wrong result'
    assert solution.maxVowels('abciiidef', 3) == 3, 'wrong result'
    assert solution.maxVowels('aeiou', 2) == 2, 'wrong result'
    assert solution.maxVowels('leetcode', 3) == 2, 'wrong result'
    assert solution.maxVowels('rhythms', 4) == 0, 'wrong result'
    assert solution.maxVowels('tryhard', 4) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_vowels()
