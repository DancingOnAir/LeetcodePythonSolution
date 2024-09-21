from collections import defaultdict


class Solution:
    # 状态机
    # 大写字母的ord二进制第6位始终为0
    # 小写字母的ord二进制第6位始终为1
    # 同样1个字母的大小写ord二进制前5位一致
    # 把字母的ord二进制转为1-26, e.g. ord('a') & 31 == 0
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        state = [0] * 27
        for ch in map(ord, word):
            idx = ch & 31
            if ch & 32:
                if state[idx] == 0:
                    state[idx] = 1
                elif state[idx] == 2:
                    state[idx] = -1
                    res -= 1
            else:
                if state[idx] == 1:
                    state[idx] = 2
                    res += 1
                elif state[idx] == 0:
                    state[idx] = -1
        return res

    def numberOfSpecialChars1(self, word: str) -> int:
        if len(word) < 2:
            return 0

        flag = defaultdict(int)
        m = defaultdict(int)
        res = 0
        for c in word:
            cur = ord(c)
            if cur + 32 in m and flag[cur] == 0:
                flag[cur] = 1
                res += 1
            if cur - 32 in m:
                if flag[cur - 32] == 1:
                    res -= 1
                flag[cur - 32] = 2

            m[cur] = 1
        return res


def test_number_of_special_chars():
    solution = Solution()
    assert solution.numberOfSpecialChars("aaAbcBC") == 3, 'wrong result'
    assert solution.numberOfSpecialChars("abc") == 0, 'wrong result'
    assert solution.numberOfSpecialChars("AbBCab") == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_special_chars()
