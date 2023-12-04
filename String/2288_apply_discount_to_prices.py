class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = []
        for s in sentence.split():
            if s[0] == '$' and s[1:].isdigit():
                res.append("${:.2f}".format(float(s[1:]) * (100 - discount) / 100))
            else:
                res.append(s)
        return ' '.join(res)


def test_discount_prices():
    solution = Solution()
    assert solution.discountPrices("there are $1 $2 and 5$ candies in the shop", 50) == "there are $0.50 $1.00 and 5$ candies in the shop", 'wrong result'
    assert solution.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100) == "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$", 'wrong result'


if __name__ == '__main__':
    test_discount_prices()
