import temperatura
import kelvin
import fahrenheit


class Celsius(temperatura.Temperature):
    
	def __init__(self, temp):
		super().__init__(temp)

	def convert_to_kelvin(self):
		return kelvin.Kelvin(self._temperature + 273.15)

	def convert_to_fahrenheit(self):
		return fahrenheit.Fahrenheit((self._temperature * 1.8) + 32)

	def convert_to_celsius(self):
		return self

	@property
	def temperature(self):
		return self._temperature

	@temperature.setter
	def temperature(self, temp):
		self._temperature = temp
