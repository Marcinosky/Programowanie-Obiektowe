import temperatura
import celsius
import fahrenheit

class Kelvin(temperatura.Temperature):
    
	def __init__(self, temp):
		super().__init__(temp)

	def convert_to_kelvin(self):
		return self

	def convert_to_fahrenheit(self):
		return fahrenheit.Fahrenheit((self._temperature - 32) * 1.8 + 273.15)

	def convert_to_celsius(self):
		return self._temperature - 273.15

	@property
	def temperature(self):
		return self._temperature

	@temperature.setter
	def temperature(self, temp):
		self._temperature = temp


