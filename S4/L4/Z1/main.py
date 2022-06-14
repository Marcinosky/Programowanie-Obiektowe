"""
Klasa Pupil zawieraj ˛aca:
	• konstruktor z dwoma parametrami imi ˛e i nazwisko - wykorzystaj właściwości
	do kontroli poprawności atrybutów name i surname - ci ˛agi tekstowe składaj ˛ace
	si ˛e z co najmniej 3 liter; konstruktor powinien także definiować atrybut marks -
	słownik przechowuj ˛acy oceny (kluczem nazwa przedmiotu a wartości ˛a ocena -
	liczba rzeczywiste ze zbioru {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6});
	• complete_marks() - dodaje przedmioty oraz oceny do słownika i kontroluje ich
	poprawność (słownik uzupełnia użytkownik);
	• print_marks() - wyświetla przedmioty i oceny;
	• metoda mean() - zwraca średni ˛a z ocen,
	• __str__() - zwraca napis składaj ˛acy si ˛e z imienia i nazwiska oraz średniej ocen.

Klasa Student dziedzicz ˛aca z klasy Pupil:
	• zawiera konstruktor z parametrami wywołuj ˛acy konstruktor klasy nadrz ˛ednej z
	dodatkowym atrybutem weights - słownik z takimi samymi kluczami jak marks
	i wartościami oznaczaj ˛acymi wagi (liczby rzeczywiste z przedziału (0, 1])
	• complete_weights() - przypisuje wag ˛e dla każdego przedmiotu i kontroluje jej
	poprawność (słownik uzupełnia użytkownik);
	• zawiera przesłoni ˛et ˛a metod ˛e mean(), która ma liczyć średni ˛a ważon ˛a.
	• zawiera metod ˛e __str__() - zwraca napis składaj ˛acy si ˛e z imienia i nazwiska oraz
	średniej ocen - wykorzystaj metod ˛e klasy bazowej.

Nast ˛epnie utwórz jeden obiekt klasy Pupil i jeden klasy Student z takimi samymi ocenami i sprawdź, jak s ˛a liczone ich średnie.

Proponowany podział pracy: pierwsza osoba - klasa Pupil i jej instancje, druga osoba - klasa Student i jej instancje.
"""

import pupil
import student

pupil1 = pupil.Pupil("Arkadiusz", "Sawa")
pupil1.complete_marks("matematyka", 4)
pupil1.complete_marks("polski", 5.5)
pupil1.complete_marks("angielski", 3.5)
pupil1.complete_marks("fizyka", 2.5)
print(pupil1)

student1 = student.Student("Seweryn", "Marcinowski")
student1.complete_marks("matematyka", 4)
student1.complete_marks("polski", 5.5)
student1.complete_marks("angielski", 3.5)
student1.complete_marks("fizyka", 2.5)
student1.complete_weighs("matematyka", 1)
student1.complete_weighs("polski", 1)
student1.complete_weighs("angielski", 0.7)
student1.complete_weighs("fizyka", 0.5)
print(student1)
