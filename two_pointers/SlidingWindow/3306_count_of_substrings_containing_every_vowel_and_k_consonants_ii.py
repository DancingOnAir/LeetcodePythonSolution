from collections import Counter


class Solution:
    # 3 pointers sliding window
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt1, cnt2 = Counter(), Counter()
        l1 = l2 = res = 0
        consonants1 = consonants2 = 0
        for r, c in enumerate(word):
            if c in 'aeiou':
                cnt1[c] += 1
                cnt2[c] += 1
            else:
                consonants1 += 1
                consonants2 += 1

            while len(cnt1) == 5 and consonants1 >= k:
                if word[l1] in 'aeiou':
                    cnt1[word[l1]] -= 1
                    if cnt1[word[l1]] == 0:
                        del cnt1[word[l1]]
                else:
                    consonants1 -= 1
                l1 += 1

            while len(cnt2) == 5 and consonants2 > k:
                if word[l2] in 'aeiou':
                    cnt2[word[l2]] -= 1
                    if cnt2[word[l2]] == 0:
                        del cnt2[word[l2]]
                else:
                    consonants2 -= 1
                l2 += 1

            res += l1 - l2
        return res

    # sliding window
    def countOfSubstrings1(self, word: str, k: int) -> int:
        def helper(k):
            l = res = cnt2 = 0
            cnt1 = Counter()
            for r, c in enumerate(word):
                if c in {'a', 'e', 'i', 'o', 'u'}:
                    cnt1[c] += 1
                else:
                    cnt2 += 1

                while len(cnt1) == 5 and cnt2 >= k:
                    if word[l] in {'a', 'e', 'i', 'o', 'u'}:
                        cnt1[word[l]] -= 1
                        if cnt1[word[l]] == 0:
                            del cnt1[word[l]]
                    else:
                        cnt2 -= 1
                    l += 1
                res += l
            return res
        return helper(k) - helper(k + 1)


def test_count_of_substrings():
    solution = Solution()
    assert solution.countOfSubstrings("iqeaouqi", 2) == 3, 'wrong result'
    assert solution.countOfSubstrings("aeioqq", 1) == 0, 'wrong result'
    assert solution.countOfSubstrings("aeiou", 0) == 1, 'wrong result'
    assert solution.countOfSubstrings("ieaouqqieaouqq", 1) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_of_substrings()
