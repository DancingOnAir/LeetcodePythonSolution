from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        n = len(num)

        for i in range(n):
            while k and stk and stk[-1] > num[i]:
                stk.pop()
                k -= 1
            stk.append(num[i])

        while k:
            stk.pop()
            k -= 1

        return ''.join(stk).lstrip('0') or '0'

    def removeKdigits1(self, num: str, k: int) -> str:
        nums = [int(i) for i in num]
        stk = []
        for num in nums:
            while stk and stk[-1] > num and k:
                stk.pop()
                k -= 1
            stk.append(num)

        while k:
            stk.pop()
            k -= 1

        res = [str(i) for i in stk]
        return str(int(''.join(res))) if res else "0"


def test_remove_k_digits():
    solution = Solution()

    num1 = "1432219"
    k1 = 3
    print(solution.removeKdigits(num1, k1))

    num2 = "10200"
    k2 = 1
    print(solution.removeKdigits(num2, k2))

    num3 = "10"
    k3 = 2
    print(solution.removeKdigits(num3, k3))


if __name__ == '__main__':
    test_remove_k_digits()
