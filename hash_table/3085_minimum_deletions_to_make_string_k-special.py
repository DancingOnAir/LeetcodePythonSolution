from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word).values()
        res = float('inf')
        for x in cnt:
            cur = 0
            for y in cnt:
                if y < x:
                    cur += y
                elif y > x + k:
                    cur += y - (x + k)
            res = min(res, cur)
        return res


def test_minimum_deletions():
    solution = Solution()
    assert solution.minimumDeletions("aabcaba", 0) == 3, 'wrong result'
    assert solution.minimumDeletions("dabdcbdcdcd", 2) == 2, 'wrong result'
    assert solution.minimumDeletions("aaabaaa", 2) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_deletions()
