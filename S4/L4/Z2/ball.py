class Ball:
	def __init__(self, given_number: int):
		self._number = given_number
		self._weighed = False

	@property
	def number(self):
		return self._number

	@property
	def weighed(self):
		return self._weighed

	def cheat(self):
		self._weighed = True

	def __str__(self):
		return f"{self._number}(weighed:{self._weighed})"
