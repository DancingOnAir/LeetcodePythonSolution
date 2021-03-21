class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = dict().setdefault
        return max(i - indices(c, i+1) for i, c in enumerate(s))

    def maxLengthBetweenEqualCharacters1(self, s: str) -> int:
        memo = dict()
        res = -1
        for i, val in enumerate(s):
            if val not in memo:
                memo[val] = i
            else:
                res = max(res, i - memo[val] - 1)
        return res


def test_max_length_between_equal_characters():
    solution = Solution()
    assert solution.maxLengthBetweenEqualCharacters('aa') == 0, 'wrong result'
    assert solution.maxLengthBetweenEqualCharacters('abca') == 2, 'wrong result'
    assert solution.maxLengthBetweenEqualCharacters('cbzxy') == -1, 'wrong result'
    assert solution.maxLengthBetweenEqualCharacters('cabbac') == 4, 'wrong result'


if __name__ == '__main__':
    test_max_length_between_equal_characters()
