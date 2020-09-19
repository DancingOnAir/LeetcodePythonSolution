from typing import List
import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(int)
        for row, col in reservedSeats:
            seats[row] = seats[row] | (1 << (col - 1))

        res = 2 * n
        for reserved in seats.values():
            cnt = 0
            cnt += (reserved & int('0111100000', 2)) == 0
            cnt += (reserved & int('0000011110', 2)) == 0
            cnt += (reserved & int('0001111000', 2)) == 0 and cnt == 0
            res += (cnt - 2)
        return res

    def maxNumberOfFamilies1(self, n: int, reservedSeats: List[List[int]]) -> int:
        matrix = collections.defaultdict(list)
        for i in range(len(reservedSeats)):
            matrix[reservedSeats[i][0]].append(reservedSeats[i][1])

        res = 2 * n
        for k in matrix:
            cnt = 0
            if all(seat not in matrix[k] for seat in [2, 3, 4, 5]):
                cnt += 1
            if all(seat not in matrix[k] for seat in [6, 7, 8, 9]):
                cnt += 1
            if all(seat not in matrix[k] for seat in [4, 5, 6, 7]) and cnt == 0:
                cnt += 1
            res += (cnt - 2)

        return res


def test_max_number_of_families():
    solution = Solution()

    n1 = 3
    reservedSeats1 = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    print(solution.maxNumberOfFamilies(n1, reservedSeats1))

    n2 = 2
    reservedSeats2 = [[2, 1], [1, 8], [2, 6]]
    print(solution.maxNumberOfFamilies(n2, reservedSeats2))

    n3 = 4
    reservedSeats3 = [[4, 3], [1, 4], [4, 6], [1, 7]]
    print(solution.maxNumberOfFamilies(n3, reservedSeats3))


if __name__ == '__main__':
    test_max_number_of_families()
