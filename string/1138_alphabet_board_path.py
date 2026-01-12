class Solution:
    def alphabetBoardPath(self, target):
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)

    # simulate movements, consider current and previous character is 'z'
    def alphabetBoardPath1(self, target: str) -> str:
        x = y = 0
        res = ''
        for c in target:
            cur = ord(c) - 97
            cur_x = cur % 5
            cur_y = cur // 5

            if cur_x == x and cur_y == y:
                res += '!'
                continue

            if cur_y > y:
                res += 'D' * ((cur_y - y) if c != 'z' else (cur_y - y - 1))
            else:
                res += 'U' * (y - cur_y)

            if cur_x > x:
                res += 'R' * (cur_x - x)
            else:
                res += 'L' * (x - cur_x)

            if c == 'z' and cur_y > y:
                res += 'D'
            res += '!'

            x, y = cur_x, cur_y
        return res


def test_alphabet_board_path():
    solution = Solution()

    assert solution.alphabetBoardPath('zz') == 'DDDDD!!', 'wrong result'
    assert solution.alphabetBoardPath('leet') == 'DDR!UURRR!!DDD!', 'wrong result'
    assert solution.alphabetBoardPath('code') == 'RR!DDRR!UUL!R!', 'wrong result'


if __name__ == '__main__':
    test_alphabet_board_path()
