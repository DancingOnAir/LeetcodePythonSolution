from typing import List


class Solution:
    # https://leetcode.com/problems/candy/discuss/135698/Simple-solution-with-one-pass-using-O(1)-space
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        decrease = peak = 0
        res = increase = 1
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                increase += 1
                peak = increase
                res += increase
                decrease = 0
            elif ratings[i - 1] > ratings[i]:
                decrease += 1
                res += decrease + (1 if peak <= decrease else 0)
                increase = 1
            else:
                increase = 1
                decrease = peak = 0
                res += 1
        return res

    # two loops: from left to right and from right to left
    def candy1(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                res[i + 1] = max(res[i] + 1, res[i + 1])
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)


def test_candy():
    solution = Solution()
    assert solution.candy([1, 0, 2]) == 5, 'wrong result'
    assert solution.candy([1, 2, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_candy()
