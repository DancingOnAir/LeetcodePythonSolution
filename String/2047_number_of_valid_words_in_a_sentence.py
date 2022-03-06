class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(word):
            num_hyphen = 0

            for i, ch in enumerate(word):
                if ch.isdigit():
                    return False
                if ch.isalpha():
                    continue
                if ch == '-':
                    num_hyphen += 1
                    if num_hyphen > 1:
                        return False
                    if i == 0 or i == len(word) - 1 or not word[i - 1].isalpha() or not word[i + 1].isalpha():
                        return False
                elif i < len(word) - 1:
                    return False
            return True
        return sum(valid(w) for w in sentence.split())

    def countValidWords1(self, sentence: str) -> int:
        res = 0
        for w in sentence.split():
            flag = 1
            num_hyphen = 0
            for i, c in enumerate(w):
                if c.isdigit():
                    flag = 0
                    break
                if c == '-':
                    if i == 0 or i == len(w) - 1 or not (w[i - 1].isalpha() and w[i + 1].isalpha()):
                        flag = 0
                        break
                    else:
                        num_hyphen += 1
                        if num_hyphen > 1:
                            flag = 0
                            break

                if c in ('!', '.', ',') and i < len(w) - 1:
                    flag = 0
                    break
            res += flag

        return res


def test_count_valid_words():
    solution = Solution()
    assert solution.countValidWords("cat and  dog") == 3, 'wrong result'
    assert solution.countValidWords("!this  1-s b8d!") == 0, 'wrong result'
    assert solution.countValidWords("cat and  dog") == 3, 'wrong result'


if __name__ == '__main__':
    test_count_valid_words()
