from collections import defaultdict


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last = defaultdict(lambda: float('-inf'))
        res = []
        for c in s:
            if len(res) - last[c] > k:
                last[c] = len(res)
                res.append(c)
        return ''.join(res)


def test_merge_characters():
    solution = Solution()
    assert solution.mergeCharacters("abca", 3) == "abc", 'wrong result'
    assert solution.mergeCharacters("aabca", 2) == "abca", 'wrong result'
    assert solution.mergeCharacters("yybyzybz", 2) == "ybzybz", 'wrong result'


if __name__ == '__main__':
    test_merge_characters()
