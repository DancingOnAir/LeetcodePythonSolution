from heapq import heappop, heappush


mx = 10_000
is_prime = [True] * mx
is_prime[1] = False
for i in range(2, mx):
    if is_prime[i]:
        for j in range(i * i, mx, i):
            is_prime[j] = False


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if is_prime[n] or is_prime[m]:
            return -1
        len_n = len(str(n))
        dist = [float('inf')] * (10 ** len_n)
        dist[n] = n
        hp = [(n, n)]
        while hp:
            dist_x, x = heappop(hp)
            if x == m:
                return dist_x
            if dist_x > dist[x]:
                continue
            v = x
            pow10 = 1
            while v:
                v, d = divmod(v, 10)
                if d > 0:
                    y = x - pow10
                    if not is_prime[y] and dist_x + y < dist[y]:
                        dist[y] = dist_x + y
                        heappush(hp, (dist_x + y, y))
                if d < 9:
                    y = x + pow10
                    if not is_prime[y] and dist_x + y < dist[y]:
                        dist[y] = dist_x + y
                        heappush(hp, (dist_x + y, y))
                pow10 *= 10
        return -1


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(1, 1) == 1, 'wrong result'
    assert solution.minOperations(10, m=12) == 85, 'wrong result'
    assert solution.minOperations(4, m=8) == -1, 'wrong result'
    assert solution.minOperations(6, m=2) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
