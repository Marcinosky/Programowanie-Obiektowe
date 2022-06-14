from abc import ABCMeta, abstractmethod

class Temperature(metaclass=ABCMeta):

	def __init__(self, temperature):
		self._temperature = temperature

	@property
	def temperature(self):
		pass

	@temperature.setter
	def temperature(self, temperature):
		pass

	@abstractmethod
	def convert_to_fahrenheit(self):
		pass

	@abstractmethod
	def convert_to_celsius(self):
		pass

	@abstractmethod
	def convert_to_kelvin(self):
		pass

	def __str__(self):
		return f"{self._temperature} stopni w skali Celsjusz"

	def __repr__(self):
		return f"{self.__class__.__name__}({self._temperature})"
		
	def above_freezing(self):
		return self._temperature > 0


