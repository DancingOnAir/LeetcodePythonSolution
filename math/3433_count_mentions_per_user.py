from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0] * numberOfUsers
        state = [0] * numberOfUsers

        for tp, ts, mention in sorted(events, key=lambda x: (int(x[1]), x[0][2])):
            cur_t = int(ts)
            if tp[0] == "O":
                state[int(mention)] = cur_t + 60
            elif mention[0] == 'A':
                for i in range(numberOfUsers):
                    res[i] += 1
            elif mention[0] == 'H':
                for i, t in enumerate(state):
                    if t <= cur_t:
                        res[i] += 1
            else:
                for s in mention.split():
                    res[int(s[2:])] += 1
        return res


def test_count_mentions():
    solution = Solution()
    assert solution.countMentions(2, [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"],
                                      ["MESSAGE", "71", "HERE"]]) == [2, 2], "wrong result"
    assert solution.countMentions(2,
                                  [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]) == [
               2, 2], "wrong result"
    assert solution.countMentions(2, [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]) == [0, 1], "wrong result"


if __name__ == '__main__':
    test_count_mentions()

