from collections import Counter

import string


class Solution:
    def sortString(self, s: str) -> str:
        def generate_key(c, cnt=dict()):
            p = cnt[c] = cnt.get(c, -1) + 1
            return p, ord(c) * (-1) ** p

        return ''.join(sorted(s, key=generate_key))

    def sortString2(self, s: str) -> str:
        cnt = Counter(s)
        res = list()
        asc = True

        while len(res) < len(s):
            for i in range(26):
                c = string.ascii_lowercase[i if asc else ~i]
                if cnt[c] > 0:
                    res.append(c)
                    cnt[c] -= 1
            asc = not asc
        return ''.join(res)

    def sortString1(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        res = ''
        i = 0
        while i < n:
            for j in range(26):
                if i > n:
                    break
                if freq[j] > 0:
                    freq[j] -= 1
                    res += chr(j + 97)
                    i += 1

            for j in range(25, -1, -1):
                if i > n:
                    break
                if freq[j] > 0:
                    freq[j] -= 1
                    res += chr(j + 97)
                    i += 1
        return res


def test_sort_string():
    solution = Solution()
    assert solution.sortString('aaaabbbbcccc') == 'abccbaabccba', 'wrong result'
    assert solution.sortString('rat') == 'art', 'wrong result'
    assert solution.sortString('leetcode') == 'cdelotee', 'wrong result'
    assert solution.sortString('ggggggg') == 'ggggggg', 'wrong result'
    assert solution.sortString('spo') == 'ops', 'wrong result'


if __name__ == '__main__':
    test_sort_string()
