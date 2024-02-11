from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass


def test_predict_party_victory():
    solution = Solution()
    assert solution.predictPartyVictory("RD") == "Radiant", 'wrong result'
    assert solution.predictPartyVictory("RDD") == "Dire", 'wrong result'


if __name__ == '__main__':
    test_predict_party_victory()
