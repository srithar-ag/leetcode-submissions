import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.index = 1
        self.lock = threading.Lock()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.index <= self.n:
            with self.lock:
                if self.index % 3 == 0 and self.index % 5 != 0 and self.index <= self.n:
                    printFizz()
                    self.index += 1

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.index <= self.n:
            with self.lock:
                if self.index % 5 == 0 and self.index % 3 != 0 and self.index <= self.n:
                    printBuzz()
                    self.index += 1

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.index <= self.n:
            with self.lock:
                if self.index % 15 == 0 and self.index <= self.n:
                    printFizzBuzz()
                    self.index += 1

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.index <= self.n:
            with self.lock:
                if self.index % 3 != 0 and self.index % 5 != 0 and self.index <= self.n:
                    printNumber(self.index)
                    self.index += 1