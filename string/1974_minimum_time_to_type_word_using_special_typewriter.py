class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        prev = 'a'

        for c in word:
            diff = abs(ord(c) - ord(prev))
            res += min(diff, 26 - diff)
            prev = c

        return res


def test_min_time_to_type():
    solution = Solution()

    assert solution.minTimeToType("abc") == 5, 'wrong result'
    assert solution.minTimeToType("bza") == 7, 'wrong result'
    assert solution.minTimeToType("zjpc") == 34, 'wrong result'


if __name__ == '__main__':
    test_min_time_to_type()
