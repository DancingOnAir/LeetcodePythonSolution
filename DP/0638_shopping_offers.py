from typing import List


class Solution:
    # dp, but TLE
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        l = len(price)
        for i in range(l, 6):
            price.append(0)
            needs.append(0)

        for i in range(len(special))[::-1]:
            special_price = special[i][l]
            special[i][l] = 0

            for j in range(l + 1, 7):
                special[i].append(0)
            special[i][6] = special_price

        dp = [[[[[([0] * 7) for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                for k in range(7):
                    for p in range(7):
                        for q in range(7):
                            for r in range(7):
                                dp[i][j][k][p][q][r] = i * price[0] + j * price[1] + k * price[2] + p * price[3] + q * price[4] + r * price[5]

        for idx in range(len(special)):
            for i in range(special[idx][0], 7):
                for j in range(special[idx][1], 7):
                    for k in range(special[idx][2], 7):
                        for p in range(special[idx][3], 7):
                            for q in range(special[idx][4], 7):
                                for r in range(special[idx][5], 7):
                                    val = dp[i - special[idx][0]][j - special[idx][1]][k - special[idx][2]][p - special[idx][3]][q - special[idx][4]][r - special[idx][5]]
                                    dp[i][j][k][p][q][r] = min(dp[i][j][k][p][q][r], val + special[idx][6])
        return dp[needs[0]][needs[1]][needs[2]][needs[3]][needs[4]][needs[5]]

    # backtracking + memory
    def shoppingOffers2(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(special, needs):

            if str(needs) in mem:
                return mem[needs]
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
            if not special:
                return sum(price[i] * needs[i] for i in range(l))

            res = float('inf')
            for s in special:
                res = min(res, s[-1] + shopping(special, [needs[i] - s[i] for i in range(l)]))

            mem[str(needs)] = res
            return res

        l = len(price)
        mem = dict()
        special =list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(l)), special))
        return shopping(special, needs)

    # backtracking
    def shoppingOffers1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(special, needs):
            if not sum(needs):
                return 0
            # filter out the number of item in specific special is greater than needs
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(len(price))), special))
            if not special:
                return sum(price[i] * needs[i] for i in range(len(price)))
            res = list()
            for s in special:
                res.append(s[-1] + shopping(special, [needs[i] - s[i] for i in range(len(price))]))
            return min(res)

        # find cost-efficient special discount
        special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(len(price))), special))
        return shopping(special, needs)


def test_shopping_offers():
    solution = Solution()

    # assert solution.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14, "wrong result"
    # assert solution.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11, "wrong result"
    assert solution.shoppingOffers([1, 1, 1], [[1, 1, 0, 0], [2, 2, 1, 0]], [1, 1, 1]) == 1, "wrong result"


if __name__ == '__main__':
    test_shopping_offers()
