from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
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

    assert solution.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14, "wrong result"
    assert solution.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11, "wrong result"


if __name__ == '__main__':
    test_shopping_offers()
