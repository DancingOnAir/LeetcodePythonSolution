from typing import List
from collections import Counter


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        c = Counter()
        for i, sender in enumerate(senders):
            c[sender] += len(messages[i].split())

        res = sorted(c.keys(), key=lambda x: (c[x], x))
        return res[-1]


def test_largest_word_count():
    solution = Solution()
    assert solution.largestWordCount(["tP x M VC h lmD","D X XF w V","sh m Pgl","pN pa","C SL m G Pn v","K z UL B W ee","Yf yo n V U Za f np","j J sk f qr e v t","L Q cJ c J Z jp E","Be a aO","nI c Gb k Y C QS N","Yi Bts","gp No g s VR","py A S sNf","ZS H Bi De dj dsh","ep MA KI Q Ou"], ["OXlq","IFGaW","XQPeWJRszU","Gb","HArIr","Gb","FnZd","FnZd","HArIr","OXlq","IFGaW","XQPeWJRszU","EMoUs","Gb","EMoUs","EMoUs"]) == "FnZd", 'wrong result'
    assert solution.largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"]) == "Alice", 'wrong result'
    assert solution.largestWordCount(["How is leetcode for everyone","Leetcode is useful for practice"], ["Bob","Charlie"]) == "Charlie", 'wrong result'


if __name__ == '__main__':
    test_largest_word_count()
