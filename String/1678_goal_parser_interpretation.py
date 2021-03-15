class Solution:
    def interpret(self, command: str) -> str:
        res, i = [], 0

        while i < len(command):
            c = command[i]
            if c == 'G':
                res += ['G']
                i += 1
            elif c == '(' and command[i + 1] == ')':
                res += ['o']
                i += 2
            else:
                res += ['al']
                i += 4

        return ''.join(res)

    def interpret1(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


def test_interpret():
    solution = Solution()
    assert solution.interpret('G()(al)') == 'Goal', 'wrong result'
    assert solution.interpret('G()()()()(al)') == 'Gooooal', 'wrong result'
    assert solution.interpret('(al)G(al)()()G') == 'alGalooG', 'wrong result'


if __name__ == '__main__':
    test_interpret()
