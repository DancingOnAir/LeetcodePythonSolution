import re


class Solution:
    def freqAlphabets(self, s: str) -> str:
        entity_symbol_list = [(str(i) if i < 10 else str(i)+'#', chr(i + 96)) for i in range(26, 0, -1)]

        for pat, rep in entity_symbol_list:
            s = s.replace(pat, rep)
        return s

    def freqAlphabets1(self, s: str) -> str:
        entity_symbol_list = [(str(i) if i < 10 else str(i)+'#', chr(i + 96)) for i in range(1, 27)]

        for pat, rep in reversed(entity_symbol_list):
            s = re.sub(pat, rep, s)
        return s


def test_freq_alphabets():
    solution = Solution()
    assert solution.freqAlphabets('10#11#12') == 'jkab', 'wrong result'
    assert solution.freqAlphabets('1326#') == 'acz', 'wrong result'
    assert solution.freqAlphabets('25#') == 'y', 'wrong result'
    assert solution.freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#') == 'abcdefghijklmnopqrstuvwxyz', 'wrong result '


if __name__ == '__main__':
    test_freq_alphabets()
