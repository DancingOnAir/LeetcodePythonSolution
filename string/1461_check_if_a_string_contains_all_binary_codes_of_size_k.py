from collections import deque


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i-k: i] for i in range(k, len(s) + 1)}) == 1 << k

    def hasAllCodes3(self, s: str, k: int) -> bool:
        seen = set()
        q = deque()
        for c in s:
            q.append(c)
            if len(q) == k:
                seen.add(''.join(q))
                q.popleft()

        return len(seen) == 1 << k

    def hasAllCodes2(self, s: str, k: int) -> bool:
        n = len(s)
        if n <= k:
            return False
        memo = set()
        for i in range(k, n+1):
            memo.add(s[i-k:i])
        return len(memo) == 2 ** k

    # TLE
    def hasAllCodes1(self, s: str, k: int) -> bool:
        n = len(s)
        if n <= k:
            return False

        for i in range(1 << k):
            cur_binary = '{:b}'.format(i)
            cur_binary = '0' * (k - len(cur_binary)) + cur_binary
            if cur_binary not in s:
                return False
        return True


def test_has_all_codes():
    solution = Solution()
    assert solution.hasAllCodes('00110110', 2), 'wrong result'
    assert solution.hasAllCodes('00110', 2), 'wrong result'
    assert solution.hasAllCodes('0110', 1), 'wrong result'
    assert not solution.hasAllCodes('0110', 2), 'wrong result'
    assert not solution.hasAllCodes('0000000001011100', 4), 'wrong result'


if __name__ == '__main__':
    test_has_all_codes()
