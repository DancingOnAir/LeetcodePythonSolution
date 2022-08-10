from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
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
