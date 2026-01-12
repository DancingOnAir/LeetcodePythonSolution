from typing import List


class Solution:
    # monotone stack
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        def pre_sum(nums):
            stk, ps = [], []
            total = 0

            for x in nums:
                cnt = 1
                while stk and stk[-1][0] > x:
                    v, c = stk.pop()
                    total -= v * c
                    cnt += c
                stk.append((x, cnt))
                total += x * cnt
                ps.append(total)
            return ps

        left = [0] + pre_sum(heights)
        right = pre_sum(heights[::-1])[::-1] + [0]
        return max(l + r for l, r in zip(left, right))


def test_maximum_sum_of_heights():
    solution = Solution()
    assert solution.maximumSumOfHeights([5, 3, 4, 1, 1]) == 13, 'wrong result'
    assert solution.maximumSumOfHeights([6, 5, 3, 9, 2, 7]) == 22, 'wrong result'
    assert solution.maximumSumOfHeights([3, 2, 5, 5, 2, 3]) == 18, 'wrong result'


if __name__ == '__main__':
    test_maximum_sum_of_heights()
