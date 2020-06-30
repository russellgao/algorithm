class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_out) == 0:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if len(self.stack_out) != 0:
            return self.stack_out.pop()
        return -1

if __name__ == "__main__" :
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    obj.appendTail(3)
    assert obj.deleteHead() == 1
    assert obj.deleteHead() == 2
    obj.appendTail(4)
    assert obj.deleteHead() == 3
    assert obj.deleteHead() == 4
    assert obj.deleteHead() == -1