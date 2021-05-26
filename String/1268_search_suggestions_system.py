from typing import List
from bisect import bisect_left


class Trie:
    def __init__(self):
        self.children = dict()
        self.suggestion = list()


class Solution:
    def _insert(self, product: str, root: Trie) -> None:
        trie = root
        for c in product:
            if c not in trie.children:
                trie.children[c] = Trie()
            trie = trie.children[c]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()

    def _search(self, searchWord: str, root: Trie) -> List[str]:
        res = list()
        for c in searchWord:
            if root:
                root = root.children.get(c)
            res.append(root.suggestion if root else [])
        return res

    # trie
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for p in products:
            self._insert(p, root)
        return self._search(searchWord, root)

    # binary search
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
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
