from collections import Counter


class Solution:
    # https://leetcode.com/problems/count-complete-substrings/solutions/4367368/python-code/
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def helper(s):
            cnt = 0
            for i in range(1, 27):
                sz = i * k
                if len(s) < sz:
                    break

                c = Counter(s[:sz])
                freq = Counter(c.values())
                if freq[k] == i:
                    cnt += 1

                for j in range(sz, len(s)):
                    freq[c[s[j]]] -= 1
                    c[s[j]] += 1
                    freq[c[s[j]]] += 1

                    freq[c[s[j - sz]]] -= 1
                    c[s[j - sz]] -= 1
                    freq[c[s[j - sz]]] += 1

                    if freq[k] == i:
                        cnt += 1
            return cnt

        res = pre = 0
        n = len(word)
        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i - 1])) > 2:
                res += helper(word[pre: i])
                pre = i

        res += helper(word[pre:])
        return res


def test_count_complete_substrings():
    solution = Solution()
    assert solution.countCompleteSubstrings("aaa", 1) == 3, 'wrong result'
    assert solution.countCompleteSubstrings("igigee", 2) == 3, 'wrong result'
    assert solution.countCompleteSubstrings("aaabbbccc", 3) == 6, 'wrong result'


if __name__ == '__main__':
    test_count_complete_substrings()
