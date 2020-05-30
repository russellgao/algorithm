import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = threading.Semaphore(1)
        self.lock2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):

            self.lock1.acquire()
            printFoo()
            self.lock2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock2.acquire()
            printBar()
            self.lock1.release()
