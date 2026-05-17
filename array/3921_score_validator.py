class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        cnt = score = 0
        for x in events:
            if x == 'W':
                cnt += 1
                if cnt == 10:
                    break
            elif x == 'WD' or x == 'NB':
                score += 1
            else:
                score += int(x)
        return [score, cnt]


def test_score_validator():
    solution = Solution()
    assert solution.scoreValidator(["1", "4", "W", "6", "WD"]) == [12, 1], 'wrong result'
    assert solution.scoreValidator(["WD", "NB", "0", "4", "4"]) == [10, 0], 'wrong result'
    assert solution.scoreValidator(["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]) == [0, 10], 'wrong result'


if __name__ == '__main__':
    test_score_validator()
