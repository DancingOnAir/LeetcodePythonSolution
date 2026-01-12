from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c1, c2 = Counter(s), Counter(target)
        return min(c1[k] // v for k, v in c2.items())


def test_rearrange_characters():
    solution = Solution()
    assert solution.rearrangeCharacters("ilovecodingonleetcode", "code") == 2, 'wrong result'
    assert solution.rearrangeCharacters("abcba", "abc") == 1, 'wrong result'
    assert solution.rearrangeCharacters("abbaccaddaeea", "aaaaa") == 1, 'wrong result'


if __name__ == '__main__':
    test_rearrange_characters()
