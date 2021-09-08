import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = list()
        for cnt, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if cnt:
                heapq.heappush(max_heap, (cnt, token))

        res = list()
        while max_heap:
            cnt, token = heapq.heappop(max_heap)
            if len(res) > 1 and token == res[-1] == res[-2]:
                if not max_heap:
                    break
                # heapreplace(a,x)返回最初在a中的最小值,而不管x的值如何,顾名思义,heappushpop(a,x)在弹出最小值之前将x推送到a上.使用您的数据,这是一个显示差异的序列：
                cnt, token = heapq.heapreplace(max_heap, (cnt, token))

            res.append(token)
            if cnt + 1:
                heapq.heappush(max_heap, (cnt + 1, token))
        return ''.join(res)

    def longestDiverseString1(self, a: int, b: int, c: int, aa: str = 'a', bb: str = 'b', cc: str = 'c') -> str:
        if a < b:
            return self.longestDiverseString(b, a, c, bb, aa, cc)
        if b < c:
            return self.longestDiverseString(a, c, b, aa, cc, bb)
        if not b:
            return aa * min(2, a)

        use_a = min(2, a)
        use_b = 1 if a - use_a >= b else 0
        return aa * use_a + bb * use_b + self.longestDiverseString(a - use_a, b - use_b, c, aa, bb, cc)


def test_longest_diverse_string():
    solution = Solution()

    assert solution.longestDiverseString(1, 1, 7) == "ccaccbcc", "wrong result"
    assert solution.longestDiverseString(2, 2, 1) == "aabbc", "wrong result"
    assert solution.longestDiverseString(7, 1, 0) == "aabaa", "wrong result"


if __name__ == '__main__':
    test_longest_diverse_string()
