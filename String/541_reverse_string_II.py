from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        for i in range(len(s))[::2*k]:
            if i + k <= len(s):
                res += s[i: i + k][::-1]
            else:
                res += s[i: len(s)][::-1]
                break

            if i + 2*k <= len(s):
                res += s[i+k: i + 2*k]
            else:
                res += s[i+k: len(s)]
        return res


def test_reverse_str():
    solution = Solution()

    assert solution.reverseStr('abcdefg', 2) == 'bacdfeg', "wrong result"


if __name__ == '__main__':
    test_reverse_str()
