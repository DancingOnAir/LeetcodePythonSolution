from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        m = dict()
        i = 1
        for e in equations:
            a, b = e[0], e[3]
            if a in m:
                x = m[a]
            else:
                m[a] = i
                x = i
                i += 1

            if b in m:
                y = m[b]
            else:
                if e[1] == '=':
                    m[b] = x
                    y = x
                else:
                    m[b] = i
                    y = i
                    i += 1

            if e[1] == '=' and x != y:
                return False
            elif e[1] == '!' and x == y:
                return False

        return True


def test_equations_possible():
    solution = Solution()
    assert not solution.equationsPossible(["a==b", "b!=a"]), 'wrong result'
    assert solution.equationsPossible(["b==a", "a==b"]), 'wrong result'
    assert solution.equationsPossible(["a==b", "b==c", "a==c"]), 'wrong result'
    assert not solution.equationsPossible(["a==b", "b!=c", "c==a"]), 'wrong result'
    assert solution.equationsPossible(["c==c", "b==d", "x!=z"]), 'wrong result'


if __name__ == '__main__':
    test_equations_possible()
