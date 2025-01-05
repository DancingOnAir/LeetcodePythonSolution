from collections import Counter


class FrequencyTracker:
    def __init__(self):
        self.cnt = Counter()
        self.freq = Counter()

    def add(self, number: int, delta=1) -> None:
        self.freq[self.cnt[number]] -= 1
        self.cnt[number] += delta
        self.freq[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number]:
            self.add(number, -1)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


def test_frequency_tracker():
    obj = FrequencyTracker()
    obj.add(3)
    obj.add(3)
    assert obj.hasFrequency(2), 'wrong result'
    assert not obj.hasFrequency(4), 'wrong result'


if __name__ == '__main__':
    test_frequency_tracker()
