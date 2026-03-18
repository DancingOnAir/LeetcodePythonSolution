from collections import Counter
from string import ascii_lowercase


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        left = Counter(s)
        for c in target:
            left[c] -= 1

        neg, mx = 0, ''
        for c, v in left.items():
            if v < 0:
                neg += 1
            elif v > 0:
                mx = max(mx, c)

        for i in range(len(s) - 1, -1, -1):
            c = target[i]
            left[c] += 1

            if left[c] == 0:
                neg -= 1
            elif left[c] == 1:
                mx = max(mx, c)

            if neg > 0 or c >= mx:
                continue
            # 寻找比当前target[i]大的s可用的字符
            j = ord(c) - ord('a') + 1
            while left[ascii_lowercase[j]] == 0:
                j += 1

            ch = ascii_lowercase[j]
            left[ch] -= 1
            res = list(target[: i + 1])
            res[i] = ch

            for ch in ascii_lowercase:
                res.extend(ch * left[ch])
            return ''.join(res)
        return ""


def test_lex_greater_permutation():
    solution = Solution()
    assert solution.lexGreaterPermutation("abc", target="bba") == "bca", "wrong result"
    assert solution.lexGreaterPermutation("leet", target="code") == "eelt", "wrong result"
    assert solution.lexGreaterPermutation("baba", target="bbaa") == "", "wrong result"


if __name__ == '__main__':
    test_lex_greater_permutation()
