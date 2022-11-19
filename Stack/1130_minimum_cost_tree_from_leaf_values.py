from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1: i] + arr[i + 1: i + 2]) * arr.pop(i)
        return res

    # intuition, remove element from smallest to bigger.
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            idx = arr.index(min(arr))
            if 0 < idx < len(arr) - 1:
                res += min(arr[idx - 1], arr[idx + 1]) * arr[idx]
            else:
                res += (arr[1] if idx == 0 else arr[-2]) * arr[idx]
            arr.pop(idx)
        return res


def test_mct_from_leaf_values():
    solution = Solution()
    assert solution.mctFromLeafValues([6, 2, 4]) == 32, 'wrong result'
    assert solution.mctFromLeafValues([4, 11]) == 44, 'wrong result'


if __name__ == '__main__':
    test_mct_from_leaf_values()

