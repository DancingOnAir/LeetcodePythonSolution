from collections import Counter
from string import ascii_lowercase


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        l1, l2 = len(c1), len(c2)

        for k1 in ascii_lowercase:
            for k2 in ascii_lowercase:
                if c1[k1] and c2[k2]:
                    if l1 == l2:
                        return True
                    else:
                        cnt1, cnt2 = l1, l2
                        if c1[k1] == 1:
                            cnt1 -= 1
                        if c1[k2] == 0:
                            cnt1 += 1
                        if c2[k1] == 0:
                            cnt2 += 1
                        if c2[k2] == 1:
                            cnt2 -= 1
                        if cnt1 == cnt2:
                            return True
        return False


def test_is_it_possible():
    solution = Solution()
    assert not solution.isItPossible("ac", "b"), 'wrong result'
    assert solution.isItPossible("abcc", "aab"), 'wrong result'
    assert solution.isItPossible("abcde", "fghij"), 'wrong result'


if __name__ == '__main__':
    test_is_it_possible()
