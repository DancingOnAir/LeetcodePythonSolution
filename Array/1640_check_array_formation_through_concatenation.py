from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = dict()

        for p in pieces:
            d[p[0]] = p

        cur = 0
        while cur < len(arr):
            char = arr[cur]
            if char in d and arr[cur: cur + len(d[char])] == d[char]:
                cur += len(d[char])
            else:
                return False
        return True


def test_can_form_array():
    solution = Solution()

    arr1 = [85]
    pieces1 = [[85]]
    assert solution.canFormArray(arr1, pieces1), "wrong result"

    arr2 = [15, 88]
    pieces2 = [[88], [15]]
    assert solution.canFormArray(arr2, pieces2), "wrong result"

    arr3 = [49, 18, 16]
    pieces3 = [[16, 18, 49]]
    assert not solution.canFormArray(arr3, pieces3), "wrong result"

    arr4 = [91, 4, 64, 78]
    pieces4 = [[78], [4, 64], [91]]
    assert solution.canFormArray(arr4, pieces4), "wrong result"

    arr5 = [1, 3, 5, 7]
    pieces5 = [[2, 4, 6, 8]]
    assert not solution.canFormArray(arr5, pieces5), "wrong result"


if __name__ == '__main__':
    test_can_form_array()
