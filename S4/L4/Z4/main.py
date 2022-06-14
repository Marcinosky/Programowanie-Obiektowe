"""
Zaprojektuj klas ˛e SortedList - przechowuj ˛aca list ˛e elementów posortowanych w kolejności. Klasa powinna być oparta o abstrakcyjn ˛a klas ˛e bazow ˛a
Sequence z modułu collections.abc. Klasa powinna tworzyć posortowan ˛a list ˛e elementów w oparciu o opcjonalny klucz (key) sortowania. Stworzona klas powinna mieć
interfejs zbliżony do wybudowanego typu list - (bez metod insert(), reverse() oraz
sort()). Zamiast metody append() zastosuj metod ˛e add() wstawiaj ˛aca dany element
w odpowiednie miejsce - w tym celu wykorzystaj metod ˛e chronion ˛a _find_index(),
która zwraca odpowiedni ˛a pozycje indeksu (zastosuj algorytm wyszukiwania binarnego)). Metody, które powinna implementować klasa SortedList:
	• __init__();
	• key() - właściwość zwracaj ˛aca klucz sortowania;
	• clear();
	• _find_index();
	• add();
	• pop();
	• remove();
	• remove_every() - usuwa wszystkie wskazane elementy (takie same) z listy;
	• __delitem__();
	• __getitem__();
	• __setitem__();
	---------------------------------------------------------------------------
	• __iter__();
	• __reversed__();
	• __contains__();
	• __len__();
	• __str__();
	• copy();
	• __copy__();
	• extend();
	• count();
	• index();
	• index().

Proponowany podział pracy: pierwsza osoba - połowa metod, druga osoba - druga połowa metod.
"""

from _collections_abc import Sequence
import sortedlist

lista = [5,4,1,16,12,65]
sortlist = sortedlist.SortedList(given_list=lista)


print(sortlist.elements)
sortlist[4] = 40							#[1, 4, 5, 12, 16, 65]
print(sortlist.elements)
del sortlist[4]
print(sortlist.elements)
i = iter(sortlist.elements)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(reversed(sortlist))
print(sortlist.__contains__(1))
len(sortlist)
print(str(sortlist))
sortlist2 = sortlist.copy()


print(type(sortlist2))
print(type(sortlist))
sortlist.extend((1, 2, 3, 4))
print(sortlist)
print(sortlist.count(1))
print(sortlist.index(4))
