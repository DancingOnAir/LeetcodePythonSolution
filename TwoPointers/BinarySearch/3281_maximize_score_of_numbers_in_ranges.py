from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(score):
            x = float('-inf')
            for s in start:
                x = max(x + score, s)
                if x > s + d:
                    return False
            return True

        left, right = 0, (start[-1] + d - start[0]) // (len(start) - 1) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid

        return left


def test_max_possible_score():
    solution = Solution()
    assert solution.maxPossibleScore([6, 0, 3], 2) == 4, 'wrong result'
    assert solution.maxPossibleScore([2, 6, 13, 13], 5) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_possible_score()
