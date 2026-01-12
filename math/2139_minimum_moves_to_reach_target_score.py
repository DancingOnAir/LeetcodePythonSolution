class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and maxDoubles > 0:
            res += 1 + (target & 1)
            maxDoubles -= 1
            target >>= 1
        return res + target - 1

    def minMoves1(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target >>= 1
                maxDoubles -= 1
            elif maxDoubles > 0:
                target -= 1
            else:
                return res + target - 1
            res += 1
        return res


def test_min_moves():
    solution = Solution()
    # assert solution.minMoves(656101987, 1) == 4, 'wrong result'
    assert solution.minMoves(5, 0) == 4, 'wrong result'
    assert solution.minMoves(19, 2) == 7, 'wrong result'
    assert solution.minMoves(10, 4) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_moves()
