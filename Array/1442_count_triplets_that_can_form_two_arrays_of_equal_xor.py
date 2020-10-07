from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr) - 1):
            accu = arr[i]
            for k in range(i + 1, len(arr)):
                accu ^= arr[k]
                if not accu:
                    res += k - i
        return res

    # Assume a == b, thus
    # a ^ a = b ^ a, thus
    # 0 = b ^ a, thus
    # arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
    # prefix[k + 1] = prefix[i]
    def countTriplets1(self, arr: List[int]) -> int:
        pre_sum = [0]
        for a in arr:
            pre_sum.append(a ^ pre_sum[-1])

        res = 0
        for i in range(len(pre_sum)):
            for j in range(i + 1, len(pre_sum)):
                if pre_sum[i] == pre_sum[j]:
                    res += j - i - 1
        return res


def test_count_triplets():
    solution = Solution()

    arr1 = [2, 3, 1, 6, 7]
    print(solution.countTriplets(arr1))

    arr2 = [1, 1, 1, 1, 1]
    print(solution.countTriplets(arr2))

    arr3 = [2, 3]
    print(solution.countTriplets(arr3))

    arr4 = [1, 3, 5, 7, 9]
    print(solution.countTriplets(arr4))

    arr5 = [7, 11, 12, 9, 5, 2, 7, 17, 22]
    print(solution.countTriplets(arr5))


if __name__ == '__main__':
    test_count_triplets()
