from collections import Counter


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''.join(c if c.isdigit() else ' ' for c in word)
        return len(Counter(map(int, s.split())))


    def numDifferentIntegers1(self, word: str) -> int:
        replaced_str = ''
        for c in word:
            if c.isdigit():
                replaced_str += c
            else:
                replaced_str += ' '

        c = Counter(replaced_str.split(' '))
        res = set()
        for k, v in c.items():
            if k.isdigit():
                res.add(int(k))
        return len(res)


def test_num_differnet_integers():
    solution = Solution()
    assert solution.numDifferentIntegers('a123bc34d8ef34') == 3, 'wrong result'
    assert solution.numDifferentIntegers('leet1234code234') == 2, 'wrong result'
    assert solution.numDifferentIntegers('a1b01c001') == 1, 'wrong result'


if __name__ == '__main__':
    test_num_differnet_integers()
