from concurrent.futures import thread

import ball
import random
from time import sleep
import threading


class LotteryMachine:
	def __init__(self):
		self.balls = []
		numbers = random.sample(range(1, 50), 49)
		for n in range(49):
			self.balls.append(ball.Ball(numbers[n]))
		tampered = random.sample(range(49), 6)
		for i in tampered:
			self.balls[i].cheat()
		self._loop = True
		
	def numbers(self):
		return self._numbers

	def wypisz(self):
		for i in range(49):
			if bool(self.balls[i].weighed):
				print(f"{self.balls[i].number}(oszustwo)")
			else:
				print(self.balls[i].number)

	def start(self):
		t = threading.Thread(target=self.shuffle)
		t.start()
		
	def shuffle(self):
		while self._loop:
			rand = random.sample(range(49), 2)
			self.balls[rand[0]], self.balls[rand[1]] = self.balls[rand[1]], self.balls[rand[0]]
			for i in range(49):
				if self.balls[i].weighed:
					if i != 0:
						self.balls[i-1], self.balls[i] = self.balls[i], self.balls[i-1]
			sleep(0.1)

	def stop(self):
		print("Stopping the shuffle")
		self._loop = False
		return self.balls[:6]

