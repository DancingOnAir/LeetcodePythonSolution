class Solution:
    def punishmentNumber(self, n: int) -> int:
        def valid(i, tot):
            if i == len(s) and tot == 0:
                return True

            for j in range(i, len(s)):
                x = int(s[i: j + 1])
                if x > tot:
                    break

                tot -= x
                if valid(j + 1, tot):
                    return True
                tot += x

            return False

        res = 0
        for i in range(1, n + 1):
            s = str(i * i)
            if valid(0, i):
                res += i * i
        return res


def test_punishment_number():
    solution = Solution()
    assert solution.punishmentNumber(10) == 182, 'wrong result'
    assert solution.punishmentNumber(37) == 1478, 'wrong result'


if __name__ == '__main__':
    test_punishment_number()
