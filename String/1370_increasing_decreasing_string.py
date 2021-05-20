class Solution:
    def sortString(self, s: str) -> str:
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
