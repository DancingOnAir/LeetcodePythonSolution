from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        cnt = defaultdict(int)
        vowels = []
        for i, c in enumerate(s):
            if c in 'aeiou':
                if c not in cnt:
                    vowels.append(c)
                cnt[c] += 1
        # stable sort
        vowels.sort(key=lambda c: -cnt[c])

        res = list(s)
        j = 0
        for i, c in enumerate(res):
            if c in 'aeiou':
                cur = vowels[j]
                res[i] = cur
                cnt[cur] -= 1
                if cnt[cur] == 0:
                    j += 1
        return ''.join(res)


def test_sort_vowels():
    solution = Solution()
    assert solution.sortVowels("leetcode") == "leetcedo", 'wrong result'
    assert solution.sortVowels("aeiaaioooa") == "aaaaoooiie", 'wrong result'
    assert solution.sortVowels("baeiou") == "baeiou", 'wrong result'


if __name__ == '__main__':
    test_sort_vowels()
