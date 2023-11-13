from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        c, stk, res = Counter(s), [], []
        for ch in s:
            stk.append(ch)
            if c[ch] == 1:
                c.pop(ch)
            else:
                c[ch] -= 1

            while c and stk and min(c) >= stk[-1]:
                res.append(stk.pop())
        res += stk[::-1]
        return ''.join(res)

    # TLE
    def robotWithStrin1(self, s: str) -> str:
        res, left, right = [], [], list(s)
        i = 0

        while left or right:
            if right:
                mi = min(right)
                if not left or mi < left[-1]:
                    res.append(mi)
                    j = right.index(mi)
                    left += right[:j]
                    right = right[j + 1:]
                else:
                    res.append(left.pop())
            else:
                res.append(left.pop())

        return ''.join(res)


def test_robot_with_string():
    solution = Solution()
    assert solution.robotWithString("cbacabacb") == "aaabbccbc", 'wrong result'
    assert solution.robotWithString("zza") == "azz", 'wrong result'
    assert solution.robotWithString("bac") == "abc", 'wrong result'


if __name__ == '__main__':
    test_robot_with_string()
