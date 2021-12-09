from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq = defaultdict(int)
        for x in range(lowLimit, highLimit+1):
            freq[sum(map(int, str(x)))] += 1
        return max(freq.values())


def test_count_balls():
    solution = Solution()

    assert solution.countBalls(1, 10) == 2, 'wrong result'
    assert solution.countBalls(5, 15) == 2, 'wrong result'
    assert solution.countBalls(19, 28) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_balls()
