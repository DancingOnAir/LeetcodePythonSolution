class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        start = 'a'
        for c in word:
            gap = abs(ord(c) - ord(start))
            res += min(gap, 26 - gap)
            start = c

        return res + len(word)


def test_min_time_to_type():
    solution = Solution()

    assert solution.minTimeToType("abc") == 5, 'wrong result'
    assert solution.minTimeToType("bza") == 7, 'wrong result'
    assert solution.minTimeToType("zjpc") == 34, 'wrong result'


if __name__ == '__main__':
    test_min_time_to_type()
