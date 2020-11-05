from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m * k:
            return False

        for i in range(n - m * k + 1):
            if arr[i: i + m] * k == arr[i: i + m * k]:
                return True
        return False


def test_contains_pattern():
    solution = Solution()

    arr1 = [1, 2, 4, 4, 4, 4]
    m1 = 1
    k1 = 3
    print(solution.containsPattern(arr1, m1, k1))
    assert solution.containsPattern(arr1, m1, k1) == True, "wrong result"

    arr2 = [1, 2, 1, 2, 1, 1, 1, 3]
    m2 = 2
    k2 = 2
    print(solution.containsPattern(arr2, m2, k2))
    assert solution.containsPattern(arr2, m2, k2) == True, "wrong result"

    arr3 = [1, 2, 1, 2, 1, 3]
    m3 = 2
    k3 = 3
    print(solution.containsPattern(arr3, m3, k3))
    assert solution.containsPattern(arr3, m3, k3) == False, "wrong result"

    arr4 = [1, 2, 3, 1, 2]
    m4 = 2
    k4 = 2
    print(solution.containsPattern(arr4, m4, k4))
    assert solution.containsPattern(arr4, m4, k4) == False, "wrong result"

    arr5 = [2, 2, 2, 2]
    m5 = 2
    k5 = 3
    print(solution.containsPattern(arr5, m5, k5))
    assert solution.containsPattern(arr5, m5, k5) == False, "wrong result"


if __name__ == '__main__':
    test_contains_pattern()
