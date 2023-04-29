class Solution:
    def addMinimum(self, word: str) -> int:
        if len(set(word)) == 1:
            return len(word) * 2

        res = 0
        stk = [word[0]]
        if word[0] == 'b':
            res += 1
        elif word[0] == 'c':
            res += 2
        for i in range(1, len(word)):
            if (stk[-1] == 'a' and word[i] == 'b') or (stk[-1] == 'b' and word[i] == 'c') or (stk[-1] == 'c' and word[i] == 'a'):
                stk.append(word[i])
                continue
            if stk[-1] == 'a' and word[i] == 'a':
                res += 2
            elif stk[-1] == 'a' and word[i] == 'c':
                res += 1
            elif stk[-1] == 'b' and word[i] == 'a':
                res += 1
            elif stk[-1] == 'b' and word[i] == 'b':
                res += 2
            elif stk[-1] == 'c' and word[i] == 'b':
                res += 1
            elif stk[-1] == 'c' and word[i] == 'c':
                res += 2
            stk.append(word[i])
        if stk[-1] == 'a':
            res += 2
        elif stk[-1] == 'b':
            res += 1
        return res


def test_add_minimum():
    solution = Solution()
    assert solution.addMinimum("b") == 2, 'wrong result'
    assert solution.addMinimum("aaa") == 6, 'wrong result'
    assert solution.addMinimum("abc") == 0, 'wrong result'


if __name__ == '__main__':
    test_add_minimum()
