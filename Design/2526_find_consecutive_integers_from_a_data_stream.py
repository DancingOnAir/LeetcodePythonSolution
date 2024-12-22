class DataStream:
    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.cnt += 1
        else:
            self.cnt = 0
        return self.cnt >= self.k


def test_data_stream():
    obj = DataStream(4, 3)
    assert not obj.consec(4), 'wrong result'
    assert not obj.consec(4), 'wrong result'
    assert obj.consec(4), 'wrong result'
    assert not obj.consec(3), 'wrong result'


if __name__ == '__main__':
    test_data_stream()
