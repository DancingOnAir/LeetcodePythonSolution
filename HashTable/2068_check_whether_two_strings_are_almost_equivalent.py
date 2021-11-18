from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c = (Counter(word1) - Counter(word2)) | (Counter(word2) - Counter(word1))
        return all(v < 4 for v in c.values()) if len(c) > 0 else True


def test_check_almost_equivalent():
    solution = Solution()

    assert not solution.checkAlmostEquivalent("aaaa", "bccb"), 'wrong result'
    assert solution.checkAlmostEquivalent("abcdeef", "abaaacc"), 'wrong result'
    assert solution.checkAlmostEquivalent("cccddabba", "babababab"), 'wrong result'


if __name__ == '__main__':
    test_check_almost_equivalent()
