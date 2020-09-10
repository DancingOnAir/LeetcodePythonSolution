from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stk = []

        for i in range(len(T)):
            while stk and T[i] > T[stk[-1]]:
                cur = stk.pop()
                res[cur] = i - cur
            stk.append(i)
        return res

    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        stk = []
        res = []
        for i in range(len(T) - 1, -1, -1):
            while stk and T[stk[-1]] <= T[i]:
                stk.pop()

            res.append(stk[-1] - i if stk else 0)
            stk.append(i)
        return res[::-1]


def test_daily_temperatures():
    solution = Solution()

    t1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures(t1))

    t2 = [73]
    print(solution.dailyTemperatures(t2))


if __name__ == '__main__':
    test_daily_temperatures()
