from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0

        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res


def test_count_good_triplets():
    solution = Solution()

    arr1 = [3, 0, 1, 1, 9, 7]
    a1 = 7
    b1 = 2
    c1 = 3
    print(solution.countGoodTriplets(arr1, a1, b1, c1))

    arr2 = [1, 1, 2, 2, 3]
    a2 = 0
    b2 = 0
    c2 = 1
    print(solution.countGoodTriplets(arr2, a2, b2, c2))


if __name__ == '__main__':
    test_count_good_triplets()
