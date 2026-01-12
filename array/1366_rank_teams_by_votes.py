from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {x: [0] * len(votes[0]) + [x] for x in votes[0]}
        for vote in votes:
            for i, val in enumerate(vote):
                count[val][i] -= 1
        return ''.join(sorted(votes[0], key=count.get))

    def rankTeams1(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        counts = {}
        for vote in votes:
            for i, c in enumerate(vote):
                if c in counts:
                    counts[c].append(i)
                else:
                    counts[c] = [i]

        sorted_counts = sorted(counts.items(), key=lambda item: (sorted(item[1]), item[0]))
        res = ''
        for k, _ in sorted_counts:
            res += k
        return res


def test_rank_teams():
    solution = Solution()

    votes1 = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    print(solution.rankTeams(votes1))

    votes2 = ["WXYZ", "XYZW"]
    print(solution.rankTeams(votes2))

    votes3 = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
    print(solution.rankTeams(votes3))

    votes4 = ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]
    print(solution.rankTeams(votes4))

    votes5 = ["M", "M", "M", "M"]
    print(solution.rankTeams(votes5))


if __name__ == '__main__':
    test_rank_teams()
