from typing import List
from itertools import accumulate


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pre_sum = list(accumulate(arr))
        res, count = 0, 0
        num_of_even_sum, num_of_odd_sum = 0, 0
        for s in pre_sum:
            if s & 1:
                res += 1
                num_of_odd_sum += 1
                res += num_of_even_sum
            else:
                num_of_even_sum += 1
                res += num_of_odd_sum

        return res % (10 ** 9 + 7)

    # brute force, but TLE
    def numOfSubarrays1(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1):
                if sum(arr[j:i+1]) & 1:
                    res += 1
        return res


def test_num_of_subarrays():
    solution = Solution()

    arr1 = [1, 3, 5]
    print(solution.numOfSubarrays(arr1))

    arr2 = [2, 4, 6]
    print(solution.numOfSubarrays(arr2))

    arr3 = [1, 2, 3, 4, 5, 6, 7]
    print(solution.numOfSubarrays(arr3))

    arr4 = [100, 100, 99, 99]
    print(solution.numOfSubarrays(arr4))

    arr5 = [7]
    print(solution.numOfSubarrays(arr5))


if __name__ == '__main__':
    test_num_of_subarrays()
