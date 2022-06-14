"""
Opracuj abstrakcyjn ˛a klas ˛e bazow ˛a o nazwie Temperature, która
przechowuje pojedyncz ˛a wartość temperatury. Klasa powinna mieć nast ˛epuj ˛acy nagłówek metody __init__() (rzeczywiście zaimplementowana metoda abstrakcyjna):
def __init__ (self, temperature)

Oprócz tego abstrakcyjna klasa Temperature powinna zawierać nast ˛epuj ˛ace metody:
	• __str__() - powinien zwrócić ci ˛ag postaci "75 stopni w skali Celsjusz" (metoda
	konkretna);
	• __repr__() - powinien zwrócić ci ˛ag postaci "ClassName(temperature)" (metoda
	konkretna);
	• above_freezing() - zwraca True jeśli temperatura powyżej punktu zamarzania
	(metoda konkretna);
	• convert_to_Fahrenheit() - zwraca nowy obiekt temperatury przekształcony na
	stopnie Fahrenheita (metoda abstrakcyjna) tj. instancj ˛e klasy Fahrenheit();
	• convert_to_Celsius() - zwraca nowy obiekt temperatury przekształcony na
	stopnie Celsjusza (metoda abstrakcyjna) tj. instancj ˛e klasy Celsius();
	• convert_to_Kelvin() - zwraca nowy obiekt temperatury przekształcony na
	stopnie Kelvina (metoda abstrakcyjna) tj. instancj ˛e klasy Kelvin(;
	• właściwości temperature typu setter i getter (abstrakcyjne właściwości).

Opracuj podklasy Fahrenheit, Celsius i Kelvin i odpowiednio wdróż każd ˛a z metody
abstrakcyjnej klasy Temperature. (Należy pami ˛etać, że gdy stosowana jest bezsensowna metoda konwersji, np. wywołanie metody, temp1.convert_to_Fahrenheit(), gdzie
temp1 jest instancj ˛a klasy Fahrenheit, powinno zwracać ten sam obiekt temperatury.

Sprawdź poprawność swoich klas w nast ˛epuj ˛acy sposób:
	• stwórz list ˛e zawieraj ˛ac ˛a 12 instancji klas (każdej po cztery egzemplarze) Kelvin,
	Celsius i Fahrenheit;
	• wydrukuj obiekty listy, a dla temperatur które s ˛a powyżej temperatury zamarzania wody dodaj adnotacj ˛e "powyżej zera";
	• utwórz trzy listy zawieraj ˛ace każd ˛a temperatur ˛e z pierwotnej listy przekształcon ˛a
	do wspólnej skali temperatur (Fahrenheita, Celsjusza, lub Kelvina);
	• z każdej z utworzonych list wydrukuj tylko te, które s ˛a poniżej temperatury zamarzania wody.

Oto potrzebne przeliczniki:
	Celsjusz = 0.556 * ( Fahrenheit - 32.0)
	Kelwin = Celsjusz + 273.16

Proponowany podział pracy: pierwsza osoba - klasy Temperature oraz Celsius, druga osoba - klasy Fahrenheit i Kelvin oraz program testuj ˛acy

"""

import temperatura, celsius, kelvin, fahrenheit

temperatures = [
	kelvin.Kelvin(155),
	kelvin.Kelvin(270),
	kelvin.Kelvin(400),
	kelvin.Kelvin(326),
	celsius.Celsius(36.3),
	celsius.Celsius(21),
	celsius.Celsius(-10),
	celsius.Celsius(100),
	fahrenheit.Fahrenheit(54),
	fahrenheit.Fahrenheit(72),
	fahrenheit.Fahrenheit(120),
	fahrenheit.Fahrenheit(5),
	]

Kelvin = temperatures.copy()
Celsius = temperatures.copy()
Fahrenheit = temperatures.copy()

for each in Kelvin:
	each.temperature() = each.convert_to_kelvin()

for each in Celsius:
	each = each.convert_to_celsius()

for each in Fahrenheit:
	each = each.convert_to_fahrenheit()

	print(temperatures)
	print(Kelvin)
	print(Celsius)
	print(Fahrenheit)