import lotterymachine
from time import sleep


class LottoPresenter:

    def __init__(self):
        self._shuffle_time = input("Witajcie w losowaniu!\nPodaj czas w sekundach, przez jaki maja byc losowane kule: ")

    def main(self):
        print("Zaczynamy Losowanie!")
        lm = lotterymachine.LotteryMachine()
        lm.start()
        sleep(int(self._shuffle_time))
        winning_numbers = lm.stop()
        print(f"The winning numbers are: {[ball.__str__() for ball in winning_numbers]}")


