class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # 'a' - '0' == 49
        def numeric_total(s: str):
            # return int(''.join([str(ord(c) - 97) for c in s]))
            return int(''.join([chr(ord(c) - 49) for c in s]))
        return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWord)

    def isSumEqual1(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_num(s: str):
            res = 0
            for c in s:
                res = res * 10 + (ord(c) - 97)
            return res

        return get_num(firstWord) + get_num(secondWord) == get_num(targetWord)


def test_is_sum_equal():
    solution = Solution()
    assert solution.isSumEqual('j', 'j', 'bi'), 'wrong result'
    assert solution.isSumEqual('acb', 'cba', 'cdb'), 'wrong result'
    assert not solution.isSumEqual('aaa', 'a', 'aab'), 'wrong result'
    assert solution.isSumEqual('aaa', 'a', 'aaaa'), 'wrong result'


if __name__ == '__main__':
    test_is_sum_equal()
