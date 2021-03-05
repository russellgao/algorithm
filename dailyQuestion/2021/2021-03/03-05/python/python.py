class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inQueue = []
        self.outQueue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inQueue.append(x)

    def in2out(self):
        if not self.outQueue:
            for i in range(len(self.inQueue)):
                self.outQueue.append(self.inQueue.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outQueue:
            self.in2out()
        x = self.outQueue.pop()
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outQueue:
            self.in2out()
        return self.outQueue[len(self.outQueue) - 1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inQueue) == 0 and len(self.outQueue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()