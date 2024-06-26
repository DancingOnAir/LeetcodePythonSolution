from typing import List
from bisect import bisect_left


class Solution:
    # https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/solutions/2569308/yu-chu-li-hui-wen-shu-zhong-wei-shu-tan-7j0zy/
    def minimumCost(self, nums: List[int]) -> int:
        def generate_palindromic_num():
            pals = []
            base = 1

            while base <= 10000:
                # 奇数长度回文字
                for i in range(base, base * 10):
                    x = i
                    t = i // 10
                    while t:
                        x = x * 10 + t % 10
                        t //= 10
                    pals.append(x)
                # 偶数长度回文字
                if base <= 1000:
                    for i in range(base, base * 10):
                        x = t = i
                        while t:
                            x = x * 10 + t % 10
                            t //= 10
                        pals.append(x)
                base *= 10
            pals.append(1_000_000_001)
            return pals

        def cost(i):
            return sum(abs(x - pals[i]) for x in nums)

        pals = generate_palindromic_num()
        nums.sort()
        mid = nums[len(nums) // 2]
        i = bisect_left(pals, mid)
        if pals[i] <= mid:
            return cost(i)
        return min(cost(i - 1), cost(i))

    def minimumCost1(self, nums: List[int]) -> int:
        def cost(x):
            return sum(abs(a - x) for a in nums)

        nums.sort()
        mid = nums[len(nums) // 2]
        decease = increase = mid
        while str(decease) != str(decease)[::-1]:
            decease -= 1
        while str(increase) != str(increase)[::-1]:
            increase += 1

        return min(cost(decease), cost(increase))


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([4, 3, 1]) == 3, 'wrong result'
    assert solution.minimumCost([1, 2, 3, 4, 5]) == 6, 'wrong result'
    assert solution.minimumCost([10, 12, 13, 14, 15]) == 11, 'wrong result'
    assert solution.minimumCost([22, 33, 22, 33, 22]) == 22, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
