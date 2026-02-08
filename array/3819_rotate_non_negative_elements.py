from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [float('inf')] * n
        non_neg = []
        for i, x in enumerate(nums):
            if x < 0:
                res[i] = x
            else:
                non_neg.append((i, x))

        m = len(non_neg)
        for i, (_, x) in enumerate(non_neg):
            res[non_neg[(i - k) % m][0]] = x
        return res


def test_rotate_elements():
    solution = Solution()
    assert solution.rotateElements([1, -2, 3, -4], k=3) == [3, -2, 1, -4], 'wrong result'
    assert solution.rotateElements([-3, -2, 7], k=1) == [-3, -2, 7], 'wrong result'
    assert solution.rotateElements([5, 4, -9, 6], k=2) == [6, 5, -9, 4], 'wrong result'


if __name__ == '__main__':
    test_rotate_elements()
