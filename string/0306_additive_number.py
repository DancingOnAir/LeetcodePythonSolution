from itertools import combinations


class Solution:
    # itertools.combinations
    def isAdditiveNumber(self, num: str) -> bool:
        def valid(a, b, s):
            if a != str(int(a)) or b != str(int(b)):
                return False
            if not s:
                return True
            c = str(int(a) + int(b))
            return s.startswith(c) and valid(b, c, s[len(c):])
        return any(valid(num[:i], num[i:j], num[j:]) for i, j in combinations(range(1, len(num)), 2))

    def isAdditiveNumber1(self, num: str) -> bool:
        def get_next_pos(start, first_len, second_len):
            if start + first_len + second_len == len(num):
                return True

            first = int(num[start: start + first_len])
            second = int(num[start + first_len: start + first_len + second_len])
            for l3 in range(max(first_len, second_len), len(num) + 1 - first_len - second_len):
                if l3 > 1 and num[start + first_len + second_len] == '0':
                    break

                third = int(num[start + first_len + second_len: start + first_len + second_len + l3])
                if first + second < third:
                    break
                elif first + second == third:
                    start += first_len
                    return get_next_pos(start, second_len, l3)
            return False

        for l1 in range(1, len(num) - 1):
            for l2 in range(1, len(num) - l1):
                if l2 > 1 and num[l1] == '0':
                    break

                if get_next_pos(0, l1, l2):
                    return True
        return False


def test_is_additive_number():
    solution = Solution()
    assert solution.isAdditiveNumber('101'), 'wrong result'
    assert solution.isAdditiveNumber('112358'), 'wrong result'
    assert solution.isAdditiveNumber('199100199'), 'wrong result'


if __name__ == '__main__':
    test_is_additive_number()
