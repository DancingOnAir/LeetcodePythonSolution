class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')

    def furthestDistanceFromOrigin1(self, moves: str) -> int:
        random, cur = 0, 0
        for x in moves:
            if x == 'L':
                cur -=1
            elif x == 'R':
                cur += 1
            else:
                random += 1
        return abs(cur) + random


def test_furthest_distance_from_origin():
    solution = Solution()
    assert solution.furthestDistanceFromOrigin("L_RL__R") == 3, 'wrong result'
    assert solution.furthestDistanceFromOrigin("_R__LL_") == 5, 'wrong result'
    assert solution.furthestDistanceFromOrigin("_______") == 7, 'wrong result'


if __name__ == '__main__':
    test_furthest_distance_from_origin()
