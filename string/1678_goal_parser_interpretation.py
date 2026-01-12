class Solution:
    # robust dictionary solution
    def interpret(self, command: str) -> str:
        d = {'G': 'G', '()': 'o', '(al)': 'al'}
        res, tmp = '', ''
        for c in command:
            tmp += c
            if tmp in d:
                res += d[tmp]
                tmp = ''
        return res

    # python list join
    def interpret2(self, command: str) -> str:
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

    # string replace
    def interpret1(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


def test_interpret():
    solution = Solution()
    assert solution.interpret('G()(al)') == 'Goal', 'wrong result'
    assert solution.interpret('G()()()()(al)') == 'Gooooal', 'wrong result'
    assert solution.interpret('(al)G(al)()()G') == 'alGalooG', 'wrong result'


if __name__ == '__main__':
    test_interpret()
