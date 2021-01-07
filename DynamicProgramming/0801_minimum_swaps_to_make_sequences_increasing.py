from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0

        swap, not_swap = 1, 0

        for i in range(1, n):
            not_swap_temp, swap_temp = n, n
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap_temp = swap + 1
                not_swap_temp = not_swap

            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap_temp = min(swap_temp, not_swap + 1)
                not_swap_temp = min(not_swap_temp, swap)

            swap, not_swap = swap_temp, not_swap_temp
        return min(swap, not_swap)

    def minSwap1(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0

        swap = [1] + [0] * (n - 1)
        not_swap = [0] * n
        for i in range(1, n):
            if (A[i - 1] < A[i] and B[i - 1] < B[i]) and (A[i - 1] < B[i] and B[i - 1] < A[i]):
                swap[i] = min(swap[i - 1], not_swap[i - 1]) + 1
                not_swap[i] = min(swap[i - 1], not_swap[i - 1])
            elif A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = swap[i - 1] + 1
                not_swap[i] = not_swap[i - 1]
            else:
                swap[i] = not_swap[i - 1] + 1
                not_swap[i] = swap[i - 1]

        return min(swap[n - 1], not_swap[n - 1])


def test_min_swap():
    solution = Solution()

    A1 = [1, 3, 5, 4]
    B1 = [1, 2, 3, 7]
    assert solution.minSwap(A1, B1) == 1, 'wrong result'

    A2 = [0, 3, 5, 8, 9]
    B2 = [2, 1, 4, 6, 9]
    assert solution.minSwap(A2, B2) == 1, 'wrong result'

    A3 = [3, 3, 8, 9, 10]
    B3 = [1, 7, 4, 6, 8]
    assert solution.minSwap(A3, B3) == 1, 'wrong result'

    A4 = [0, 4, 4, 5, 9]
    B4 = [0, 1, 6, 8, 10]
    assert solution.minSwap(A4, B4) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_swap()
