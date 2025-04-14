class Solution:
    # concise
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i, c in enumerate(s) if c != '0')
        s[0], s[i] = s[i], s[0]
        return int(''.join(s))

    def smallestNumber1(self, num: int) -> int:
        if num == 0:
            return num

        if num > 0:
            res = sorted(str(num))
            for i, c in enumerate(res):
                if c != '0':
                    res[0], res[i] = res[i], res[0]
                    break
            return int(''.join(res))

        res = sorted((str(-num)), reverse=True)
        return -int(''.join(res))


def test_smallest_number():
    solution = Solution()
    assert solution.smallestNumber(310) == 103, 'wrong result'
    assert solution.smallestNumber(-7605) == -7650, 'wrong result'


if __name__ == '__main__':
    test_smallest_number()
