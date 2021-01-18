from typing import List


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
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
