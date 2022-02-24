from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()]
        heapify(pq)

        res = list()
        while pq:
            k, v = heappop(pq)
            if res and res[-1] == k:
                if not pq:
                    break
                kk, vv = heappop(pq)
                res.append(kk)
                if vv - 1:
                    heappush(pq, (kk, vv - 1))
                heappush(pq, (k, v))
            else:
                m = min(v, repeatLimit)
                res.extend([k] * m)
                if v - m:
                    heappush(pq, (k, v - m))

        return ''.join(chr(-x) for x in res)

    def repeatLimitedString1(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        k = sorted(c)

        res = ''
        while len(c) > 0:
            if c[k[-1]] <= repeatLimit:
                if k[-1] == 's':
                    print(k[-1])

                res += k[-1] * c[k[-1]]

                del c[k[-1]]
                k.pop()
            else:
                res += k[-1] * repeatLimit
                c[k[-1]] -= repeatLimit

                if len(k) == 1:
                    break
                res += k[-2]
                c[k[-2]] -= 1
                if c[k[-2]] == 0:
                    del c[k[-2]]
                    k.pop(-2)

        return res


def test_repeat_limited_string():
    solution = Solution()
    assert solution.repeatLimitedString('xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt', 1) == 'zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba', 'wrong result'
    assert solution.repeatLimitedString('cczazcc', 3) == 'zzcccac', 'wrong result'
    assert solution.repeatLimitedString('aababab', 2) == 'bbabaa', 'wrong result'


if __name__ == '__main__':
    test_repeat_limited_string()
