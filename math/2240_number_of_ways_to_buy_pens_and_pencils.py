class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        for i in range(total // cost1 + 1):
            res += (total - i * cost1) // cost2 + 1
        return res


def test_ways_to_buy_pens_pencils():
    solution = Solution()
    assert solution.waysToBuyPensPencils(20, 10, 5) == 9, 'wrong result'
    assert solution.waysToBuyPensPencils(5, 10, 10) == 1, 'wrong result'


if __name__ == '__main__':
    test_ways_to_buy_pens_pencils()
