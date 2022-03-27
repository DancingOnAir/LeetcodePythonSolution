class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        while 'RL' in directions:
            directions = directions.replace('RL', 'SS', 1)
            res += 2
        while 'RS' in directions:
            directions = directions.replace('RS', 'SS', 1)
            res += 1
        while 'SL' in directions:
            directions = directions.replace('SL', 'SS', 1)
            res += 1
        return res


def test_count_collisions():
    solution = Solution()
    assert solution.countCollisions('RLRSLL') == 5, 'wrong result'
    assert solution.countCollisions('LLRR') == 0, 'wrong result'


if __name__ == '__main__':
    test_count_collisions()
