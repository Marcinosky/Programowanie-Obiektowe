import temperatura
import kelvin
import celsius

class Fahrenheit(temperatura.Temperature):
    
	def __init__(self, temp):
		super().__init__(temp)

	def convert_to_kelvin(self):
		return kelvin.Kelvin((self._temperature - 32) * 1.8 + 273.15)

	def convert_to_fahrenheit(self):
		return self

	def convert_to_celsius(self):
		return (self._temperature - 32) * 1.8

	@property
	def temperature(self):
		return self._temperature

	@temperature.setter
	def temperature(self, temp):
		self._temperature = temp


