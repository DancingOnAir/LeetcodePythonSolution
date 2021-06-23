class Solution:
    # two pointers
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        return ''.join(s)

    # stack
    def reverseOnlyLetters3(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        return ''.join(ss if not ss.isalpha() else letters.pop() for ss in s)

    def reverseOnlyLetters2(self, s: str) -> str:
        letters = ''
        for ss in s:
            if ss.isalpha():
                letters += ss
        letters = letters[::-1]
        res = ''
        i = 0
        for ss in s:
            if ss.isalpha():
                res += letters[i]
                i += 1
            else:
                res += ss
        return res

    def reverseOnlyLetters1(self, s: str) -> str:
        s = list(s)
        non_letters = dict()
        letters = list()
        for i, c in enumerate(s):
            if not c.isalpha():
                non_letters[i] = c
            else:
                letters.append(c)

        res = list()
        while len(res) < len(s):
            if len(res) in non_letters:
                res.append(non_letters[len(res)])
            else:
                res.append(letters.pop())
        return ''.join(res)


def test_reverse_only_letters():
    solution = Solution()
    assert solution.reverseOnlyLetters('ab-cd') == 'dc-ba', 'wrong result'
    assert solution.reverseOnlyLetters('a-bC-dEf-ghIj') == 'j-Ih-gfE-dCba', 'wrong result'
    assert solution.reverseOnlyLetters('Test1ng-Leet=code-Q!') == 'Qedo1ct-eeLg=ntse-T!', 'wrong result'


if __name__ == '__main__':
    test_reverse_only_letters()
