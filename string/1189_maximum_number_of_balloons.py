from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(c) // 'balloon'.count(c) for c in 'balon')

    def maxNumberOfBalloons1(self, text: str) -> int:
        n = len(text) // len('balloon')
        cnt = Counter(text)
        for i in range(n, -1, -1):
            if len(Counter('balloon' * i) - cnt) == 0:
                return i
        return 0


def test_max_number_of_balloons():
    solution = Solution()

    assert solution.maxNumberOfBalloons('nlaebolko') == 1, 'wrong result'
    assert solution.maxNumberOfBalloons('loonbalxballpoon') == 2, 'wrong result'
    assert solution.maxNumberOfBalloons('leetcode') == 0, 'wrong result'


if __name__ == '__main__':
    test_max_number_of_balloons()
