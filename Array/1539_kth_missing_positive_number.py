from typing import List
from bisect import bisect_left


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        elif k >= arr[-1]:
            return k + len(arr)

        for a in arr:
            if a <= k:
                k += 1
            else:
                return k
        return k

def test_find_Kth_positive():
    solution = Solution()

    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print(solution.findKthPositive(arr1, k1))

    arr2 = [1, 2, 3, 4]
    k2 = 2
    print(solution.findKthPositive(arr2, k2))


if __name__ == '__main__':
    test_find_Kth_positive()
