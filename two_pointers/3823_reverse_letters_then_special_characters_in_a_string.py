from typing import Callable


class Solution:
    def reverseByType(self, s: str) -> str:
        t = list(s)

        def reverse(f: Callable[[str], bool]) -> None:
            i, j = 0, len(t) - 1
            while i < j:
                while i < j and f(t[i]):
                    i += 1
                while i < j and f(t[j]):
                    j -= 1
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1

        reverse(lambda c: c.islower())
        reverse(lambda c: not c.islower())
        return ''.join(t)


def test_reverse_by_type():
    solution = Solution()
    assert solution.reverseByType(")ebc#da@f(") == "(fad@cb#e)", 'wrong result'
    assert solution.reverseByType("z") == "z", 'wrong result'
    assert solution.reverseByType("!@#$%^&*()") == ")(*&^%$#@!", 'wrong result'


if __name__ == '__main__':
    test_reverse_by_type()
