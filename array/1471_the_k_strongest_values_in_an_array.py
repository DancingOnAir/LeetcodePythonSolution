from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        median = arr[(n - 1) // 2]
        left, right = 0, n - 1
        while n + left - right <= k:
            if arr[right] - median >= median - arr[left]:
                right -= 1
            else:
                left += 1

        return arr[:left] + arr[right+1:]

    def getStrongest1(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        median = arr[(n - 1) // 2]

        res = []
        left, right = 0, n - 1
        while k > 0:
            if abs(arr[right] - median) >= abs(arr[left] - median):
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
            k -= 1

        return res


def test_get_strongest():
    solution = Solution()

    arr1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(solution.getStrongest(arr1, k1))

    arr2 = [1, 1, 3, 5, 5]
    k2 = 2
    print(solution.getStrongest(arr2, k2))

    arr3 = [6, 7, 11, 7, 6, 8]
    k3 = 5
    print(solution.getStrongest(arr3, k3))

    arr4 = [6, -3, 7, 2, 11]
    k4 = 3
    print(solution.getStrongest(arr4, k4))

    arr5 = [-7, 22, 17, 3]
    k5 = 2
    print(solution.getStrongest(arr5, k5))


if __name__ == '__main__':
    test_get_strongest()
