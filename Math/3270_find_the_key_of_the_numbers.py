class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        vals = [str(x).zfill(4) for x in (num1, num2, num3)]
        return int(''.join(map(min, zip(*vals))))

    def generateKey1(self, num1: int, num2: int, num3: int) -> int:
        res, pow10 = 0, 1
        for _ in range(4):
            res += min(num1 % 10, num2 % 10, num3 % 10) * pow10
            num1 //= 10
            num2 //= 10
            num3 //= 10
            pow10 *= 10
        return res


def test_generate_key():
    solution = Solution()
    assert solution.generateKey(1, num2=10, num3=1000) == 0, 'wrong result'
    assert solution.generateKey(987, num2=879, num3=798) == 777, 'wrong result'
    assert solution.generateKey(1, 2, 3) == 1, 'wrong result'


if __name__ == '__main__':
    test_generate_key()
