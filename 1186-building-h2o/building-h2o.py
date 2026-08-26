from threading import Semaphore
from typing import Callable


class H2O:
    def __init__(self):
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(0)
        self.hydrogen_count = 0

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.hydrogen_semaphore.acquire()
        releaseHydrogen()
        self.hydrogen_count += 1
        if self.hydrogen_count == 2:
            self.hydrogen_count = 0  
            self.oxygen_semaphore.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.oxygen_semaphore.acquire()

        releaseOxygen()
        self.hydrogen_semaphore.release()
        self.hydrogen_semaphore.release()
