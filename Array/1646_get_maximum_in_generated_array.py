from typing import List


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                arr[1] = 1
            elif i & 1:
                arr[i] = arr[i // 2] + arr[i // 2 + 1]
            else:
                arr[i] = arr[i // 2]
        return max(arr)

    def getMaximumGenerated1(self, n: int) -> int:
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                arr[i] = 1
            if 2 * i < n + 1:
                arr[2 * i] = arr[i]
            if 2 * i + 1 < n + 1:
                arr[2 * i + 1] = arr[i] + arr[i + 1]

        return max(arr)


def test_get_maximum_generated():
    solution = Solution()

    assert solution.getMaximumGenerated(7) == 3, "wrong result"
    assert(solution.getMaximumGenerated(2)) == 1, "wrong result"
    assert(solution.getMaximumGenerated(3)) == 2, "wrong result"
    assert(solution.getMaximumGenerated(4)) == 2, "wrong result"
    assert(solution.getMaximumGenerated(15)) == 5, "wrong result"


if __name__ == '__main__':
    test_get_maximum_generated()
