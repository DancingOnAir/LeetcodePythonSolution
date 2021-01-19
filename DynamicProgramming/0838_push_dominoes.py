from typing import List


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = ''
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue

            if i:
                res += dominoes[i]

            mid = j - i - 1
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * mid
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res += '.' * mid
            else:
                res += 'R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2)
            i = j

        return res

    # calculate left & right forces
    def pushDominoes2(self, dominoes: str) -> str:
        n = len(dominoes)
        if not n:
            return ''
        elif n == 1:
            return dominoes

        forces = [0] * n
        f = 0
        # right forces
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] += f
        f = 0
        # left forces
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] -= f

        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in forces)

    def pushDominoes1(self, dominoes: str) -> str:
        if not dominoes:
            return ''

        n = len(dominoes)
        if n == 1:
            return dominoes

        dp = [''] * n
        dp[0] = dominoes[0]
        for i in range(1, n):
            if dominoes[i] == 'L':
                dp[i] = 'L'

                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    j -= 1

                if j < 0:
                    dp[:i] = 'L' * i
                elif dominoes[j] == 'L':
                    dp[j:i] = 'L' * (i - j)
                elif dominoes[j] == 'R':
                    if (i - j - 1) & 0b1:
                        dp[(i+j)//2] = '.'
                    dp[(i+j)//2 + 1:i] = 'L' * ((i - j - 1) // 2)
            elif dominoes[i] == 'R':
                dp[i] = 'R'
            else:
                if dp[i - 1] == 'R':
                    dp[i] = 'R'
                else:
                    dp[i] = '.'
        return ''.join(dp)


def test_push_dominoes():
    solution = Solution()
    assert solution.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL..", 'wrong result'
    assert solution.pushDominoes("RR.L") == "RR.L", 'wrong result'


if __name__ == '__main__':
    test_push_dominoes()
