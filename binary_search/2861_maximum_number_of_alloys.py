from typing import List


class Solution:
    # stock[i] >= composition[i][j] * num, total = 0
    # stock[i] < composition[i][j] * num, total = (composition[i][j] * num - stock[j]) * cost[j]
    # num和total存在单调性，可以使用二分算法
    # 区间 [1, min(stock) + budget]
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        res = 0
        mx = min(stock) + budget
        for comp in composition:
            def check(num):
                total = 0
                for s, base, c in zip(stock, comp, cost):
                    if s < base * num:
                        total += (base * num - s) * c
                        if total > budget:
                            return False
                return True

            # 写法2
            # left, right = res, mx + 1
            # while left + 1 < right:
            #     mid = (left + right) // 2
            #     if check(mid):
            #         left = mid
            #     else:
            #         right = mid
            # res = left
            # 写法1, 注意res = mid，记录右区间
            left, right = res, mx
            while left <= right:
                mid = (left + right) // 2
                if check(mid):
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
        return res


def test_max_number_of_alloys():
    solution = Solution()
    assert solution.maxNumberOfAlloys(4, 4, 17, [[10, 10, 1, 5], [9, 7, 7, 1], [6, 3, 5, 9], [2, 10, 2, 7]],
                                      [9, 8, 2, 7], [9, 2, 6, 10]) == 1, 'wrong result'
    assert solution.maxNumberOfAlloys(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 0], [1, 2, 3]) == 2, 'wrong result'
    assert solution.maxNumberOfAlloys(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 100], [1, 2, 3]) == 5, 'wrong result'
    assert solution.maxNumberOfAlloys(2, 3, 10, [[2, 1], [1, 2], [1, 1]], [1, 1], [5, 5]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_number_of_alloys()
