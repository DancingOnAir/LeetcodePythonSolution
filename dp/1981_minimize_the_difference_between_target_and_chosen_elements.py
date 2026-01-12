from typing import List


class Solution:
    # https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/solutions/1418651/c-bitset-meh/
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # p is the bitset from 0 to max, if the bit i is 1 that means i can be the sum result by far
        p = 1
        for r in mat:
            tmp = 0
            for i in r:
                # okay, this is the trick. Instead of sums up each of the N elements of the each M rows, we make a single shift left. Magic!
                tmp |= (p << i)
            p = tmp

        res = 10000
        for i in range(p.bit_length() + 1):
            if (p >> i) & 1:
                res = min(res, abs(target - i))
        return res


def test_minimize_the_difference():
    solution = Solution()
    assert solution.minimizeTheDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13) == 0, 'wrong result'
    assert solution.minimizeTheDifference([[1], [2], [3]], 100) == 94, 'wrong result'
    assert solution.minimizeTheDifference([[1, 2, 9, 8, 7]], 6) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimize_the_difference()

