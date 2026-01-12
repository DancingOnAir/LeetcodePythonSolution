class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def greedy(s, c1, c2):
            stk = list()
            for c in s:
                if stk and stk[-1] == c1 and c == c2:
                    stk.pop()
                else:
                    stk.append(c)
            return ''.join(stk)

        a, b = 'a', 'b'
        if x < y:
            a, b = b, a
            x, y = y, x

        s1 = greedy(s, a, b)
        s2 = greedy(s1, b, a)

        return (len(s) - len(s1)) * x // 2 + (len(s1) - len(s2)) * y // 2


def test_maximum_gain():
    solution = Solution()

    assert solution.maximumGain('cdbcbbaaabab', 4, 5) == 19, 'wrong result'
    assert solution.maximumGain('aabbaaxybbaabb', 5, 4) == 20, 'wrong result'


if __name__ == '__main__':
    test_maximum_gain()
