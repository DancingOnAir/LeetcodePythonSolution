from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x * y


class Solution:
    # optimized binary search
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = list()
        left, right = 1, 1000
        for x in range(1, 1001):
            if customfunction.f(x, left) > z or customfunction.f(x, right) < z:
                continue

            yl, yr = left, right
            while yl <= yr:
                ym = yl + (yr - yl) // 2
                if customfunction.f(x, ym) == z:
                    res.append([x, ym])
                    break
                elif customfunction.f(x, ym) < z:
                    yl = ym + 1
                else:
                    yr = ym - 1

            if customfunction.f(x, yl) >= z:
                right = yl

        return res

    # binary search
    def findSolution1(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = list()
        x = 1
        while x <= 1000:
            yl, yr = 1, 1000
            while yl <= yr:
                ym = (yl + yr) // 2
                cur = customfunction.f(x, ym)
                if cur == z:
                    res.append([x, ym])
                    break
                elif cur < z:
                    yl = ym + 1
                else:
                    yr = ym - 1
            x += 1
        return res


def test_find_solution():
    solution = Solution()
    custom_function = CustomFunction()
    assert sorted(solution.findSolution(custom_function, 5)) == [[1, 5], [5, 1]], 'wrong result'
    # assert sorted(solution.findSolution(custom_function, 5)) == [[1, 4], [2, 3], [3, 2], [4, 1]], 'wrong result'


if __name__ == '__main__':
    test_find_solution()
