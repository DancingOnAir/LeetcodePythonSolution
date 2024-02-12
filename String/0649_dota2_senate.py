from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rq, dq = deque(), deque()
        for i, s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while len(rq) > 0 and len(dq) > 0:
            r = rq.popleft()
            d = dq.popleft()

            if r < d:
                rq.append(r + n)
            else:
                dq.append(d + n)
        return "Radiant" if len(rq) > 0 else "Dire"


def test_predict_party_victory():
    solution = Solution()
    assert solution.predictPartyVictory("RD") == "Radiant", 'wrong result'
    assert solution.predictPartyVictory("RDD") == "Dire", 'wrong result'


if __name__ == '__main__':
    test_predict_party_victory()
