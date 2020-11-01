from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        res = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if res < arr[i]:
                count = 0
                res = arr[i]
            count += 1
            if count == k:
                return res

        return res


def test_get_winner():
    solution = Solution()

    arr1 = [2, 1, 3, 5, 4, 6, 7]
    k1 = 2
    print(solution.getWinner(arr1, k1))

    arr2 = [3, 2, 1]
    k2 = 10
    print(solution.getWinner(arr2, k2))

    arr3 = [1, 9, 8, 2, 3, 7, 6, 4, 5]
    k3 = 7
    print(solution.getWinner(arr3, k3))

    arr4 = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    k4 = 1000000000
    print(solution.getWinner(arr4, k4))


if __name__ == '__main__':
    test_get_winner()
