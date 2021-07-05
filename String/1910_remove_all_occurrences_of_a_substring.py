class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)
        nxt = [0] * m
        j = 0
        s, part = list(s), list(part)
        for i in range(1, m):
            while j and part[i] != part[j]:
                j = nxt[j - 1]
            if part[i] == part[j]:
                j += 1
            nxt[i] = j
        print(nxt)

        stk = [('', 0)]
        for c in s:
            k = stk[-1][1]
            while k and part[k] != c:
                k = nxt[k - 1]
            if part[k] == c:
                k += 1
            stk.append((c, k))
            if k == m:
                stk = stk[: -m]
        return ''.join(x for x, _ in stk)

    def removeOccurrences1(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s


def test_remove_occurrences():
    solution = Solution()

    # assert solution.removeOccurrences('wwwwwwwwwwwwwwwwwwwwwvwwwwswxwwwwsdwxweeohapwwzwuwajrnogb', 'w') == 'dab', 'wrong result'
    assert solution.removeOccurrences('daabcbaabcbc', 'abc') == 'dab', 'wrong result'
    assert solution.removeOccurrences('axxxxyyyyb', 'xy') == 'ab', 'wrong result'


if __name__ == '__main__':
    test_remove_occurrences()
