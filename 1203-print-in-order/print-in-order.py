import threading
from typing import Callable

class Foo:
    def __init__(self):
        self.lock_for_second = threading.Lock()
        self.lock_for_third = threading.Lock()
        self.lock_for_second.acquire()
        self.lock_for_third.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.lock_for_second.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.lock_for_second.acquire()

        printSecond()
      
        self.lock_for_third.release()

    def third(self, printThird: Callable[[], None]) -> None:
        self.lock_for_third.acquire()

        printThird()
      
