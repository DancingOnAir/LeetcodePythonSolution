from collections import deque, Counter, defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        frogs = max_frogs = 0
        for c in croakOfFrogs:
            idx = d[c]
            cnt[idx] += 1

            if idx == 0:
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            elif idx == 4:
                frogs -= 1
            else:
                cnt[idx - 1] -= 1
                if cnt[idx - 1] < 0:
                    return -1
        return max_frogs if frogs == 0 else -1

    def minNumberOfFrogs1(self, croakOfFrogs: str) -> int:
        d = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        memo = [0] * 5

        res = 0
        for i, c in enumerate(croakOfFrogs):
            if c not in d:
                return -1
            idx = d[c]
            for j in range(5):
                if j < idx and memo[idx] >= memo[j]:
                    return -1
                elif j > idx and memo[idx] < memo[j]:
                    return -1

            if c == 'k':
                for j in range(4):
                    memo[j] -= 1
            else:
                memo[idx] += 1
            res = max(res, memo[0])

        if any(i for i in memo):
            return -1
        return res


def test_min_number_of_frogs():
    solution = Solution()
    assert solution.minNumberOfFrogs('croakcroak') == 1, 'wrong result'
    assert solution.minNumberOfFrogs('crcoakroak') == 2, 'wrong result'
    assert solution.minNumberOfFrogs('croakcrook') == -1, 'wrong result'
    assert solution.minNumberOfFrogs('croakcroa') == -1, 'wrong result'


if __name__ == '__main__':
    test_min_number_of_frogs()
