from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        dx, dy = 1, 1
        while dx < bound:
            dy = 1
            while dx + dy <= bound:
                res.add(dx + dy)
                if y == 1:
                    break
                dy *= y
            if x == 1:
                break
            dx *= x
        return list(res)


def test_powerful_integers():
    solution = Solution()
    assert solution.powerfulIntegers(2, 1, 10) == [2, 3, 4, 5, 7, 9, 10], 'wrong result'
    assert solution.powerfulIntegers(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10], 'wrong result'
    assert solution.powerfulIntegers(2, 5, 15) == [2, 4, 6, 8, 10, 14], 'wrong result'


if __name__ == '__main__':
    test_powerful_integers()
