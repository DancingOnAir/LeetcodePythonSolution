from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(arr[i: i+l])
        return res

    # brute force
    def sumOddLengthSubarrays1(self, arr: List[int]) -> int:
        n = len(arr)

        if n < 3:
            return sum(arr)

        res, i, count = 0, 1, 0
        while i <= n:
            for j in range(n - i + 1):
                res += sum(arr[j:j+i])

            count += 1
            i = 2 * count + 1

        return res


def test_sum_odd_length_subarrays():
    solution = Solution()

    arr1 = [1, 4, 2, 5, 3]
    print(solution.sumOddLengthSubarrays(arr1))
    assert solution.sumOddLengthSubarrays(arr1) == 58, "wrong result"

    arr2 = [1, 2]
    print(solution.sumOddLengthSubarrays(arr2))
    assert solution.sumOddLengthSubarrays(arr2) == 3, "wrong result"

    arr3 = [10, 11, 12]
    print(solution.sumOddLengthSubarrays(arr3))
    assert solution.sumOddLengthSubarrays(arr3) == 66, "wrong result"


if __name__ == '__main__':
    test_sum_odd_length_subarrays()
