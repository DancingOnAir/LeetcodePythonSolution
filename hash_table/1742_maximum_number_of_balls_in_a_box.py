from collections import defaultdict


class Solution:
    # math
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # high limit <= 10 ** 5, the max digit sum is 9 * 5 = 45
        box = [0] * 46
        idx = sum(map(int, str(lowLimit)))

        for x in range(lowLimit, highLimit+1):
            while x % 10 == 0:
                idx -= 9
                x //= 10

            box[idx] += 1
            idx += 1
        return max(box)

    # brute force
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
