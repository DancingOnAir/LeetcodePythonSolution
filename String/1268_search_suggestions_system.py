from typing import List
from bisect import bisect_left


class Solution:
    # binary search
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cur, res = '', list()
        for c in searchWord:
            cur += c
            i = bisect_left(products, cur)
            res.append([p for p in products[i:i + 3] if p.startswith(cur)])
        return res

    # brute force O(n*m)
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = list()

        for i, c in enumerate(searchWord):
            if not i:
                cur = [p for p in products if p[i] == c]
                cur.sort()
                res.append(cur[:3])
            else:
                cur = [p for p in cur if i < len(p) and p[i] == c]
                res.append(cur[:3])
        return res


def test_suggested_products():
    solution = Solution()
    assert solution.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse") == [["mobile", "moneypot", "monitor"],["mobile", "moneypot", "monitor"],["mouse", "mousepad"],["mouse", "mousepad"],["mouse", "mousepad"]], 'wrong result'

    assert solution.suggestedProducts(["havana"], "havana") == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]], 'wrong result'

    assert solution.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bags") == [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]], 'wrong result'

    assert solution.suggestedProducts(["havana"], "tatiana") == [[], [], [], [], [], [], []], 'wrong result'


if __name__ == '__main__':
    test_suggested_products()
