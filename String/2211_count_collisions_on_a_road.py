class Solution:
    # cars on left side which are moving in left direction are never going to collide,
    # Similarly, cars on right side which are moving right side are never going to collide.
    # In between them every car is going to collide.
    def countCollisions(self, directions: str) -> int:
        left = 0
        while left < len(directions) and directions[left] == 'L':
            left += 1

        right = len(directions) - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1

        res = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                res += 1
        return res

    def countCollisions1(self, directions: str) -> int:
        pre = directions[0]
        pre_num = 1
        res = 0
        for ch in directions[1:]:
            if pre == ch:
                pre_num += 1
                pre = ch
            else:
                if ch == 'L':
                    if pre == 'R':
                        res += pre_num + 1
                    elif pre == 'S':
                        res += 1
                    pre = 'S'
                elif ch == 'S':
                    if pre == 'R':
                        res += pre_num

                    pre = ch
                else:
                    pre = ch
                pre_num = 1

        return res

    # TLE
    def countCollisions1(self, directions: str) -> int:
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
