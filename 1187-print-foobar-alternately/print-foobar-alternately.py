from threading import Semaphore
from typing import Callable

class FooBar:
    def __init__(self, n: int) -> None:
        self.n = n
        self.foo_semaphore = Semaphore(1)
        self.bar_semaphore = Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.foo_semaphore.acquire()
            printFoo()
            self.bar_semaphore.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.bar_semaphore.acquire()
            printBar()
            self.foo_semaphore.release()