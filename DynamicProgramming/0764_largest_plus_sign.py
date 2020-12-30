from typing import List


class Solution:
    def validate_one(self, N, mines, x, y):
        if x < 0 or x >= N or y < 0 or y >= N or [x, y] in mines:
            return False
        return True

    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        res = 0
        for i in range(N):
            for j in range(N):
                order = 0
                if [i, j] not in mines:
                    order += 1
                    radius = 1
                    while self.validate_one(N, mines, i - radius, j) and self.validate_one(N, mines, i + radius, j) and\
                            self.validate_one(N, mines, i, j - radius) and self.validate_one(N, mines, i, j + radius):
                        order += 1
                        radius += 1
                res = max(res, order)
        return res


def test_order_of_largest_plus_sign():
    solution = Solution()

    N1 = 5
    mines1 = [[4, 2]]
    assert solution.orderOfLargestPlusSign(N1, mines1) == 2, 'wrong result'

    N2 = 2
    mines2 = []
    assert solution.orderOfLargestPlusSign(N2, mines2) == 1, 'wrong result'

    N3 = 1
    mines3 = [[0, 0]]
    assert solution.orderOfLargestPlusSign(N3, mines3) == 0, 'wrong result'


if __name__ == '__main__':
    test_order_of_largest_plus_sign()
